import src.utils.ecs as ecs
import random
import uuid
from .dynamic import DynamicTraitSystem
from .dynamic import trigger_life_event
import src.utils.constants as con
from .personality import Personality
from .traits import Trait
from .traits import TRAITS
from .traits import TRAIT_SYNERGIES
from .traits import TRAIT_EVOLUTIONS
from .traits import TRAIT_COMBOS
from .traits import TRAIT_PASSIVE_EFFECTS

class Character(ecs.entity):
    def __init__(self):
        super().__init__()
        
class Character:
    def __init__(self, name, age_group):
        self.id = uuid.uuid4()
        self.name = name
        self.age_group = age_group
        self.components = {}
        self.personality = Personality(age_group)
        self.traits = self.personality.generate()
        self.dynamic_trait_system = DynamicTraitSystem()
    
    def add_component(self, component):
        """Add a component to the character."""
        self.components[type(component)] = component
        return self

    def get_component(self, component_type):
        """Safely retrieve a component."""
        return self.components.get(component_type)

    def add_trait(self, trait):
        """Add a trait to the character."""
        if trait.trait_group not in self.traits:
            self.traits[trait.trait_group] = []
        self.traits[trait.trait_group].append(trait)

    def trigger_life_event(self, event):
        """Trigger a life event for the character."""
        trigger_life_event(self, event)

    def update_age_group(self, new_age_group):
        """Update the character's age group and adjust traits accordingly."""
        self.age_group = new_age_group
        self.personality.age_group = new_age_group
        self.personality.evolve_traits()
        # Optionally, reset or adjust components based on new age group

class Skills:
    def __init__(self, skills):
        self.skills = skills
    
    def improve_related_stats(self, skill, levels_gained, stats_component):
        """Improve stats related to a skill."""
        base_stats = stats_component.base_stats
        
        if skill.group in con.SKILL_STAT_RELATIONS:
            related_stats = con.SKILL_STAT_RELATIONS[skill.group]
            for stat in related_stats:
                base_stats[stat] += levels_gained * 0.1
                print(f"Improved {', '.join(related_stats)} from leveling up {skill.name}!")
        
        # Small chance to improve a random stat
        if random.random() < 0.05:  # 5% chance
            random_stat = random.choice(list(base_stats.keys()))
            base_stats[random_stat] += levels_gained * 0.05
            print(f"Lucky! Also improved {random_stat} a bit.")
        
        # Update advanced stats
        stats_component.update_advanced_stats()

class Stats:
    def __init__(self, base_stats):
        self.base_stats = base_stats
        self.advanced_stats = {}

    def update_advanced_stats(self):
        """Calculate advanced stats based on base stats."""
        # Implement your advanced stat calculation logic here
        for stat, value in self.base_stats.items():
            # Example: Some advanced stat calculations
            self.advanced_stats[f'{stat}_modifier'] = value * 0.1
            self.advanced_stats[f'{stat}_multiplier'] = 1 + (value * 0.01)

class SkillSystem:
    def update(self, characters):
        """Update skills for all characters."""
        for character in characters:
            skills_comp = character.get_component(Skills)
            stats_comp = character.get_component(Stats)
            
            if skills_comp and stats_comp:
                for skill in skills_comp.skills:
                    levels_gained = skill.level_up()
                    skills_comp.improve_related_stats(skill, levels_gained, stats_comp)