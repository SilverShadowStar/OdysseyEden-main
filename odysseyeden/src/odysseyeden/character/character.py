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
from src.utils.constants import AGE_GROUPS GENE_TYPES

# Making the namesets
female_names = namemaker.make_name_set("female_first_names.txt")
male_names = namemaker.make_name_set("male_first_names.txt")
last_names = namemaker.make_name_set("last_names.txt")


class Character:
    def __init__(self, age_group: str, mother: Optional['Character'] = None, father: Optional['Character'] = None, genes: Optional[dict] = None, fname: Optional[str] = None):
        self.id = uuid .uuid4()
        self.age_group = age_group
        self.mother = mother
        self.father = father
        self.genes = genes if genes is not None else self.generate_genes(mother, father)

        # Assign first name based on the second gene
        if fname is not None:
            self.fname = fname
        else:
            # Check the second gene to determine the name
            second_gene = self.genes['sex'][1]  # Get the second gene from the sex gene list
            self.fname = female_names.make_name() if second_gene == 'X' else male_names.make_name()

        self.lname = self.father.lname if self.father is not None else last_names.make_name()
        self.name = f"{self.fname} {self.lname}"
        self.components = {}
        self.personality = Personality(age_group)
        self.traits = self.personality.generate()
        self.dynamic_trait_system = DynamicTraitSystem()
    
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