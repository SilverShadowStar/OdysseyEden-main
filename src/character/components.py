import actions
import traits
import skills
import genes
import dynamic
import personality
import jobs
import stats
from src.utils.ecs import Component

class Position(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y    

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        return f"Position({self.x}, {self.y})"
    
class Sprite(Component):
    def __init__(self, image_path, x=0, y=0):
        self.image_path = image_path
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Sprite({self.image_path}, {self.x}, {self.y})"
    
class Health(Component):
    def __init__(self, max_health=100):
        self.max_health = max_health
        self.current_health = max_health
        self.alive = True

    def __repr__(self):
        return f"Health(max_health={self.max_health}, current_health={self.current_health})"

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
            self.alive = False

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def is_alive(self):
        return self.alive

    def is_dead(self):
        return not self.alive

    def __repr__(self):
        return f"Health(max_health={self.max_health}, current_health={self.current_health})"
    
class Genetics(Component):
    def __init__(self, dna):
        self.dna = dna
        self.genetic_mutations = []

    def __repr__(self):
        return f"Genetics(dna={self.dna}, genetic_mutations={self.genetic_mutations})"
    
class Personality(Component):
    def __init__(self, personality):
        self.personality = personality
        self.personality_traits = []

    def __repr__(self):
        return f"Personality(personality={self.personality}, personality_traits={self.personality_traits})"
    
class Traits(Component):
    def __init__(self, traits):
        self.traits = traits
        self.traits_values = []

    def __repr__(self):    
        return f"Traits(traits={self.traits}, traits_values={self.traits_values})"
    
class Skills(Component):
    def __init__(self, skills):
        self.skills = skills
        self.skills_values = []

    def __repr__(self):
        return f"Skills(skills={self.skills}, skills_values={self.skills_values})"
    
class Jobs(Component):
    def __init__(self, jobs):
        self.jobs = jobs
        self.jobs_values = []

    def __repr__(self):
        return f"Jobs(jobs={self.jobs}, jobs_values={self.jobs_values})"
    
class Actions(Component):
    def __init__(self, actions):
        self.actions = actions
        self.actions_values = []

    def __repr__(self):
        return f"Actions(actions={self.actions}, actions_values={self.actions_values})"

class Stats(Component):
    def __init__(self, base_stats):
        self.base_stats = base_stats
        self.stats = []
        self.stats_values = []
        self.stats_modifiers = []
        self.stats_modifiers_values = []
        
    def __repr__(self):
        return f"Stats(base_stats={self.base_stats}, stats={self.stats}, stats_values={self.stats_values}, stats_modifiers={self.stats_modifiers}, stats_modifiers_values={self.stats_modifiers_values})"
    
class Dynamic(Component):
    def __init__(self, dynamic):
        self.dynamic = dynamic
        self.dynamic_values = []

    def __repr__(self):
        return f"Dynamic(dynamic={self.dynamic}, dynamic_values={self.dynamic_values})"
    
class LifeEvents(Component):
    def __init__(self, life_events):
        self.life_events = life_events
        self.life_events_values = []

    def __repr__(self):
        return f"LifeEvents(life_events={self.life_events}, life_events_values={self.life_events_values})"
    
class Inventory(Component):
    def __init__(self, inventory):
        self.inventory = inventory
        self.inventory_values = []

    def __repr__(self):
        return f"Inventory(inventory={self.inventory}, inventory_values={self.inventory_values})"
    
class Equipment(Component):
    def __init__(self, equipment):
        self.equipment = equipment
        self.equipment_values = []

    def __repr__(self):
        return f"Equipment(equipment={self.equipment}, equipment_values={self.equipment_values})
    
