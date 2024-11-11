import logging
from dataclasses import dataclass
from typing import Dict, List, Optional
from src.utils.constants import AGES, TRAITS, TRAIT_EVOLUTIONS, TRAIT_SYNERGIES

# Configure logging
logging.basicConfig(level=logging.INFO)

@dataclass
class TraitCategory:
    name: str
    positive: List[str]
    neutral: List[str]
    negative: List[str]

class Traits:
    categories = [
        'temperament', 'socialization', 'emotional', 'interaction',
        'cognition', 'identity', 'ambition', 'morals', 'perspective', 'legacy'
    ]

    def __init__(self, num_traits_per_category=5):
        self.num_traits_per_category = num_traits_per_category
        self.traits = self.initialize_traits()
        self.evolutions = self.define_evolutions()
        self.synergies = self.define_synergies()

    def initialize_traits(self) -> Dict[str, TraitCategory]:
        """Initialize traits for each category."""
        trait_categories = {}
        for i, category in enumerate(self.categories):
            start_index = i * self.num_traits_per_category * 3  # 3 lists (positive, neutral, negative)
            trait_categories[category] = TraitCategory(
                name=category,
                positive=TRAITS[start_index:start_index + self.num_traits_per_category],
                neutral=TRAITS[start_index + self.num_traits_per_category:start_index + self.num_traits_per_category],
                negative=TRAITS[start_index + self.num_traits_per_category * 2:start_index + self.num_traits_per_category * 3]
            )
        return trait_categories

    def define_evolutions(self):
        """Define trait evolutions based on age groups."""
        return [
            # Example evolution definitions (adjust according to your game logic)
            # (Old Trait, New Trait, Age Group)
            (TRAITS[0], TRAITS[30], AGES['youth']),  # Example of temperament to emotional
            (TRAITS[1], TRAITS[31], AGES['youth']),
            # Add more evolutions as needed
        ]

    def define_synergies(self) -> List[tuple]:
        """Define trait synergies."""
        return [
            (('curious', 'inquisitive'), 'enhances learning speed for knowledge-seeking skills'),
            (('cheerful', 'optimistic'), 'boosts creativity-related skill gains'),
            # Add more synergies as needed
        ]

class Trait:
    def __init__(self, name: str, age_group: str, trait_group: str, synergy: Dict[str, str], passive_effect: Optional[str] = None) -> None:
        """
        Initialize a Trait object.

        Parameters:
        - name (str): The name of the trait.
        - age_group (str): The age group when this trait was acquired (e.g., 'Child', 'Teen').
        - trait_group (str): The category this trait belongs to (e.g., 'Personality', 'Skill').
        - synergy (dict): A dictionary mapping traits that synergize with this one.
        - passive_effect (str): A passive effect the trait provides, if any.
        """
        self.name: str = name
        self.age_group: str = age_group
        self.trait_group: str = trait_group
        self.synergy: Dict = synergy
        self.passive_effect: Optional[str] = passive_effect

    def evolve(self, current_age_group: str) -> 'Trait':
        """
        Evolve the current trait based on the character's current age group.

        Parameters:
        - current_age_group (str): The age group the character is currently in.

        Returns:
        - Trait: A new Trait instance representing the evolved trait.
        """
        if current_age_group not in [age_group for age_group, _ in TRAIT_EVOLUTIONS]:
            logging.warning(f"Invalid age group: {current_age_group}. No evolution will occur.")
            return self  # No evolution if the age group is invalid

        for evolution in TRAIT_EVOLUTIONS:
            if self.name == evolution[0] and self.age_group == evolution[1]:
                # Create a new Trait instance with the evolved name
                new_trait = Trait(name=evolution[2], age_group=current_age_group, trait_group=self.trait_group, synergy=self.synergy, passive_effect=self.passive_effect)
                logging.info(f"Evolved {self.name} to {new_trait.name}.")
                return new_trait  # Return the new evolved trait

        # If no evolution occurs, return the current instance
        return self

    def synergy_effect(self, other_trait: 'Trait') -> str:
        """
        Calculate the synergy effect with another trait.

        Parameters:
        - other_trait (Trait): The other trait to check synergy with.

        Returns:
        - str: Description of the synergy effect, if any.
        """
        synergy_key = (self.name, other_trait.name)
        if synergy_key in self.synergy:
            return f"Synergy between {self.name} and {other_trait.name}: {self.synergy[synergy_key]}"
        return "No synergy effect."

class MBTI():
	def __init__(self, name: str, trait_effect: Dict, compatibility: Dict, ):
		
"""Friendships: MBTI Compatibility Overview
Best Friends:

ENFP & INFJ: Deep emotional and intuitive bond, with a balance of creativity and wisdom.
ENTP & INTJ: Intellectual synergy; ENTP’s innovation complements INTJ’s strategic mind.
ISFJ & ESFJ: Loyal and nurturing, they share a focus on care and harmony.
ISFP & ESFP: Fun-loving and emotionally authentic, they connect over shared experiences.
Worst Enemies:

ESTJ & INFP: Clash between ESTJ’s practicality and INFP’s idealism and sensitivity.
ENTJ & ISFP: ENTJ’s forceful leadership may feel oppressive to ISFP’s values-driven, sensitive nature.
ISTJ & ENFP: ISTJ’s need for order contrasts with ENFP’s free-spirited, spontaneous nature.
Balanced but Challenging:

INTP & ENFJ: Intellectual vs. emotional focus; potential for growth but requires understanding.
ISTP & ESFJ: Pragmatic ISTP might clash with ESFJ’s social and emotional approach.
ISFJ & ENTP: Tradition and harmony (ISFJ) vs. challenge and spontaneity (ENTP).
Romantic Relationships: MBTI Compatibility Overview

Best Romance Partners:

INFJ & ENFP: Emotional depth and mutual growth, valuing personal development and intuition.
INTJ & ENFP: Opposites attract; ENFP's creativity softens INTJ’s logic, balancing emotional and strategic thinking.
ENTP & INFJ: Intellectual and emotional depth, creating a dynamic partnership.
ISFJ & ESFJ: Stable, nurturing relationships with shared values and loyalty.
Good but Challenging:

ENTJ & INFP: Strong attraction but potential conflict between ENTJ’s practicality and INFP’s idealism.
INTP & ESFJ: Analytical vs. emotional approach; can balance but requires effort.
ESTP & ISFJ: Adventure (ESTP) vs. stability (ISFJ); potential for excitement but may need compromise.
Struggling Pairings:

ISTJ & ENFP: Stability vs. spontaneity; a difficult match for long-term romance.
ESTJ & INFP: Practicality vs. emotional ideals often leads to misunderstanding.
ENTP & ISFJ: ENTP’s need for novelty clashes with ISFJ’s preference for tradition and security.
Balanced but Needs Effort:

ENFJ & ISTP: Opposite focuses (empathy vs. independence) that require communication.
INTP & ENFJ: Logical INTP and emotionally expressive ENFJ can thrive with mutual respect.
ENTP & ISTJ: Creative vs. orderly; potential to learn from each other with effort."""