#src/character/skills.py 

survival=['foraging', 'hunting', 'fishing', 'cooking', 'fire-making', 'shelter-building', 'farming', 'tool crafting', 'animal husbandry'],
combat=['melee', 'archery', 'defense', 'tactics', 'martial arts'],
crafting=['woodworking', 'stoneworking', 'metalworking', 'textile crafting', 'pottery', 'building', 'leatherworking'],
artisan= ['painting', 'writing', 'sculpting', 'music'],
communication=['bartering', 'leadership', 'teaching', 'diplomacy', 'persuasion'],
healing=['herbalisim', 'first aid', 'surgery', 'midwifery', 'spiritual healing'],
mental=['meditation', 'philosophy', 'spiritual leadership'],
exploration=['navigation', 'cartography', 'swimming', 'climbing'],
domestic=['cleaning', 'child rearing', 'clothing maintenance'],
magic=['elemental', 'divination', 'alchemy', 'enchanting']
class Skills:
    def __init__(self):
        self.learned_skills = []  # List of skills the character has learned
        self.unlearned_skills = []  # List of skills the character has not learned
        self.skill_levels = {}  # Dictionary of skill levels
        self.skill_exp = {}  # Dictionary of skill experience
        self.skill_groups = {}  # Dictionary of skill groups
    
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