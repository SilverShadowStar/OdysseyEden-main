class Component:
    """A base class for all components."""
    pass


class Entity:
    """An entity is an object that can have components attached to it."""

    def __init__(self):
        self.components = {}

    def add_component(self, component):
        """Adds a component to the entity's set of components and assigns the
        entity to the component. The component is returned after being added."""
        self.components[type(component)] = component
        return component

    def get_component(self, component_type):
        """Returns the component of the given type if the entity has it, None
        otherwise."""
        return self.components.get(component_type)

class System:
    def update(self, entities):
        """Update method to be implemented by subclasses."""
        pass

class ECS:
    """A simple ECS (Entity-Component-System) framework."""

    def __init__(self):
        self.entities = []
        self.systems = []

    def add_entity(self, entity):
        """Adds an entity to the ECS."""
        self.entities.append(entity)

    def add_system(self, system):
        """Adds a system to the ECS."""
        self.systems.append(system)

    def update(self):
        """Updates all systems in the ECS."""
        for system in self.systems:
            system.update(self.entities)

# Example components
class Position(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Health(Component):
    def __init__(self, health=100):
        self.health = health

    def damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            self.kill()

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

# Example system
class MovementSystem(System):
    def update(self, entities):
        for entity in entities:
            position = entity.get_component(Position)
            if position:
                position.x += 1  # Simple movement logic
