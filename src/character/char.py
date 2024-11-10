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





