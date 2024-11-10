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