
# dynamic_traits.py

from typing import List, Dict
import random
from .personality import Trait
from ..utils.constants import TRAITS

class DynamicTraitSystem:
    def __init__(self, life_events: Dict[str, List[str]] = None):
        """
        Initialize a DynamicTraitSystem object.

        A DynamicTraitSystem object is used to generate dynamic traits based on life events.

        The life_events dictionary maps life event keys to lists of traits that can be generated as a result of the event.
        """
        self.life_events = life_events or {
            "academic_success": ["diligent", "curious", "motivated"],
            "academic_failure": ["distracted", "complacent", "unmotivated"],
            "romantic_success": ["confident", "affectionate", "optimistic"],
            "romantic_failure": ["insecure", "cynical", "pessimistic"],
            "career_advancement": ["ambitious", "dedicated", "goal-oriented"],
            "job_loss": ["adaptable", "resilient", "unmotivated"],
            "travel_experience": ["open-minded", "adventurous", "curious"],
            "trauma": ["anxious", "cautious", "resilient"],
            "act_of_kindness": ["compassionate", "generous", "empathetic"],
            "act_of_cruelty": ["cynical", "mistrustful", "hardened"]
        }

    def get_potential_traits(self, event: str) -> List[str]:
        """
        Get a list of potential traits that can be acquired based on the given life event.

        Parameters:
        - event (str): The life event to generate traits for.

        Returns:
        - list: A list of trait names that can be acquired as a result of the life event.
        """
        return self.life_events.get(event, [])

    def acquire_trait(self, character, event: str) -> Trait:
        """
        Acquire a new trait for the character based on a life event.
    
        This function selects a potential trait from a predefined list of traits associated with 
        the specified life event. It then creates and returns a Trait object for the character 
        if the trait is found in the TRAITS dictionary.
    
        Parameters:
        - character: The character for whom the trait is being acquired.
        - event (str): The life event that may result in acquiring a new trait.
    
        Returns:
        - Trait: A new Trait object representing the acquired trait, or None if no trait is acquired.
        """
        potential_traits = self.get_potential_traits(event)
        if not potential_traits:
            return None

        new_trait_name = random.choice(potential_traits)
        if new_trait_name in TRAITS.get(character.age_group, []):
            return Trait(new_trait_name, character.age_group, "personality")

        return None

    @staticmethod
    def trigger_life_event(character, event: str) -> None:
        """
        Trigger a life event that may result in the character acquiring a new trait.

        Parameters:
        - character: The character for whom the life event is being triggered.
        - event (str): The life event to trigger.

        Returns:
        - None
        """
        trait_system = DynamicTraitSystem()
        new_trait = trait_system.acquire_trait(character, event)
        if new_trait:
            character.add_trait(new_trait)
            print(f"{character.name} experienced {event} and gained the trait: {new_trait.name}")
