import random
import uuid
import namemaker
from typing import Optional, Dict, Any
from .dynamic import DynamicTraitSystem
from .dynamic import trigger_life_event
from .personality import Personality
from .traits import Trait
from .traits import TRAITS
from .traits import TRAIT_SYNERGIES
from .traits import TRAIT_EVOLUTIONS
from .traits import TRAIT_COMBOS
from .traits import TRAIT_PASSIVE_EFFECTS
from src.utils.constants import AGE_GROUPS, GENE_TYPES

# Making the namesets
female_names = namemaker.make_name_set("female_first_names.txt")
male_names = namemaker.make_name_set("male_first_names.txt")
last_names = namemaker.make_name_set("last_names.txt")

class Inventory:
    def __init__(self):
        self.items = []  # List of items the character possesses

class Quests:
    def __init__(self):
        self.active_quests = []  # List of active quests

class Sprites:
    def __init__(self):
        self.sprite_image = None  # Placeholder for sprite image

class Character:
    def __init__(self, age: str, mother: Optional['Character'] = None, father: Optional['Character'] = None, fname: Optional[str] = None, lname: Optional[str] = None):
        self.components = {}  # Initialize the components dictionary
        self.systems = {}      # Initialize the systems dictionary

        # Add components to the dictionary
        self.components['id'] = str(uuid.uuid4())  # Unique identifier for the character
        self.components['age_group'] = AgeGroup(age)  # Age group component
        self.components['relationships'] = Relationships()  # Manages relationships with other characters
        self.components['family'] = Family(mother=mother, father=father)  # Family relationships
        self.components['genes'] = Genes(mother, father)  # Genetic traits based on parents
        self.components['names'] = Names(fname=fname, lname=lname, father=father)  # Name management
        self.components['personality'] = Personality(self.components['age_group'].group)  # Personality traits
        self.components['dynamic'] = DynamicTraitSystem()  # System for dynamic traits
        self.components['looks'] = Looks()  # Physical appearance attributes
        self.components['health'] = Health()  # Health status management
        self.components['needs'] = Needs()  # Basic needs (hunger, thirst, etc.)
        self.components['stats'] = Stats()  # Core statistics (stamina, strength, etc.)
        self.components['skills'] = Skills()  # Skills that the character can learn and improve
        self.components['jobs'] = Jobs()  # Job or career-related attributes
        self.components['actions'] = Actions()  # Possible actions the character can take
        self.components['inventory'] = Inventory()  # Items and resources the character possesses
        self.components['quests'] = Quests()  # Active quests and progress tracking
        self.components['sprites'] = Sprites()  # Visual representation (sprites) of the character
        self.components['action_queue'] = ActionQueue()  # Queue for actions to be performed

    def get_component(self, component_name):
        """Retrieve a component by name."""
        return self.components.get(component_name)

    def get_system(self, system_name):
        """Retrieve a system by name."""
        return self.systems.get(system_name)

    def generate_name(self):
        """Generate a name for the character if not provided."""
        if not self.components['names'].fname:
            second_gene = self.components['genes'].sex[1]  # Get the second gene from the sex gene list
            self.components['names'].fname = female_names.make_name() if second_gene == 'X' else male_names.make_name()
        
        if not self.components['names'].lname:
            if not self.components['family'].father:
                self.components['names'].lname = last_names.make_name()  # Generate last name if not provided

    # Additional methods can be implemented here for character actions, updates, and interactions
    def update_age(self, years):
        """Update the character's age and related components."""
        self.components['age_group'].update_age(years)
        self.components['personality'].age_group = self.components['age_group'].group
        # Handle other logic related to age change

    def generate_genes(self, mother: Optional['Character'], father: Optional['Character']) -> dict:
        """Generate genes based on the parents' genes or randomly if no parents are provided."""
        genes = {}

        # Handle the SEX gene separately
        first_gene = 'X'  # First gene is always 'X'
        second_gene = random.choice(SEX)  # Second gene can be 'X' or 'Y'
        genes['sex'] = [first_gene, second_gene]  # Store the SEX genes

        # Generate genes for other traits
        for trait, options in GENE_TYPES.items():
            if trait != 'sex':  # Skip the SEX trait as it's already handled
                if mother and father:
                    # Randomly choose from each parent's corresponding genes
                    gene1 = random.choice(mother.genes[trait])
                    gene2 = random.choice(father.genes[trait])
                else:
                    # If no parents, randomly generate two genes from the options
                    gene1 = random.choice(options)
                    gene2 = random.choice(options)

                genes[trait] = [gene1, gene2]  # Each trait gets 2 genes

        return genes  # This will return a dictionary with traits as keys and lists of genes as values

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
