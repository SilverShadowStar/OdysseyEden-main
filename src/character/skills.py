
"""perception
instinct
literacy
knowledge
creativity
mediation
cunning
persuasion
cooking
mechanical
technology
combat
endurance
stealth
survial
luck
communication
organization
animal
pacifying

agile
clumsy
naive
savvy"""

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