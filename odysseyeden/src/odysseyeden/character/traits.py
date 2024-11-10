#from src.utils.constants import AGES, TRAITS
from dataclasses import dataclass, field

AGES = {
    'infant': (0, 2),
    'sprout': (3, 4),
    'youth': (5, 12),
    'adolescent': (13, 17),
    'prime': (18, 29),
    'mature': (30, 59),
    'sage': (60, 120)
}

TRAITS = [
    'easy-going',
    'adaptable',
    'content',
    'cheerful',
    'calm',
    'active',
    'regular',
    'slow-to-warm-up',
    'moderate',
    'observant',
    'fussy',
    'irritable',
    'unpredictable',
    'restless',
    'overactive',
    'sociable',
    'playful',
    'affectionate',
    'friendly',
    'outgoing',
    'observant',
    'independent',
    'cautious',
    'curious',
    'mellow',
    'clingy',
    'irritable',
    'withdrawn',
    'hyperactive',
    'impulsive',
    'cheerful',
    'passionate',
    'optimistic',
    'joyful',
    'hopeful',
    'sensitive',
    'calm',
    'reflective',
    'balanced',
    'realistic',
    'moody',
    'anxious',
    'gloomy',
    'aggressive',
    'doubtful',
    'cooperative',
    'empathetic',
    'supportive',
    'generous',
    'trustworthy',
    'reserved',
    'independent',
    'adaptable',
    'neutral',
    'pragmatic',
    'shy',
    'confrontational',
    'manipulative',
    'aloof',
    'dismissive',
    'curious',
    'diligent',
    'creative',
    'inquisitive',
    'motivated',
    'practical',
    'analytical',
    'intuitive',
    'theoretical',
    'exploratory',
    'distracted',
    'stubborn',
    'uncritical',
    'complacent',
    'disinterested',
    'confident',
    'principled',
    'open-minded',
    'self-aware',
    'authentic',
    'questioning',
    'experimental',
    'idealistic',
    'reflective',
    'curious',
    'insecure',
    'conformist',
    'rebellious',
    'conflicted',
    'doubtful',
    'ambitious',
    'dedicated',
    'innovative',
    'goal-oriented',
    'driven',
    'flexible',
    'specialized',
    'risk-taking',
    'pragmatic',
    'adaptable',
    'unmotivated',
    'workaholic',
    'indecisive',
    'complacent',
    'disengaged',
    'honest',
    'compassionate',
    'resilient',
    'fair-minded',
    'generous',
    'traditional',
    'pragmatic',
    'individualistic',
    'balanced',
    'neutral',
    'materialistic',
    'judgmental',
    'hedonistic',
    'selfish',
    'cynical',
    'wise',
    'content',
    'grateful',
    'optimistic',
    'hopeful',
    'philosophical',
    'nostalgic',
    'accepting',
    'realistic',
    'pragmatic',
    'cynical',
    'regretful',
    'bitter',
    'despondent',
    'resentful',
    'mentoring',
    'philanthropic',
    'inspiring',
    'guiding',
    'visionary',
    'reflective',
    'private',
    'traditional',
    'conservative',
    'practical',
    'disengaged',
    'controlling',
    'resentful',
    'manipulative',
    'detached'
]

@dataclass
class TraitCategory:
    name: str
    positive: list
    neutral: list
    negative: list

class Traits:
    categories = [
        'temperament', 'socialization', 'emotional', 'interaction',
        'cognition', 'identity', 'ambition', 'morals', 'perspective', 'legacy'
    ]

    traits = {}
    per_age = {
        AGES['infant']: ['temperament'],
        AGES['sprout']: ['temperament', 'socialization'],
        AGES['youth']: ['emotional', 'interaction', 'cognition'],
        AGES['adolescent']: ['emotional', 'interaction', 'cognition', 'identity'],
        AGES['prime']: ['emotional', 'interaction', 'ambition', 'morals'],
        AGES['mature']: ['emotional', 'interaction', 'ambition', 'morals', 'perspective'],
        AGES['sage']: ['emotional', 'interaction', 'morals', 'perspective', 'legacy']
    }

    def __init__(self):
        for i, category in enumerate(self.categories):
            start_index = i * self.num_traits_per_category
            self.traits[category] = TraitCategory(
                name=category,
                positive=TRAITS[start_index:start_index + 5],
                neutral=TRAITS[start_index + 5:start_index + 10],
                negative=TRAITS[start_index + 10:start_index + 15]
            )

        self.evolutions = [
            # Temperament to Emotional
            (TRAITS['temperament']['positive'][0], TRAITS['emotional']['positive'][0], AGES['youth']),  #
            (TRAITS['temperament']['positive'][1], TRAITS['emotional']['positive'][1], AGES['youth']),  #
            (TRAITS['temperament']['positive'][2], TRAITS['emotional']['positive'][2], AGES['youth']),  #
            (TRAITS['temperament']['positive'][3], TRAITS['emotional']['positive'][3], AGES['youth']),  #
            (TRAITS['temperament']['positive'][4], TRAITS['emotional']['positive'][4], AGES['youth']),  #
            (TRAITS['temperament']['neutral'][0], TRAITS['emotional']['neutral'][0], AGES['youth']),    #
            (TRAITS['temperament']['neutral'][1], TRAITS['emotional']['neutral'][1], AGES['youth']),    #
            (TRAITS['temperament']['neutral'][2], TRAITS['emotional']['neutral'][2], AGES['youth']),    #
            (TRAITS['temperament']['neutral'][3], TRAITS['emotional']['neutral'][3], AGES['youth']),    #
            (TRAITS['temperament']['neutral'][4], TRAITS['emotional']['neutral'][4], AGES['youth']),    #
            (TRAITS['temperament']['negative'][0], TRAITS['emotional']['negative'][0], AGES['youth']),  #
            (TRAITS['temperament']['negative'][1], TRAITS['emotional']['negative'][1], AGES['youth']),  #
            (TRAITS['temperament']['negative'][2], TRAITS['emotional']['negative'][2], AGES['youth']),  #
            (TRAITS['temperament']['negative'][3], TRAITS['emotional']['negative'][3], AGES['youth']),  #
            (TRAITS['temperament']['negative'][4], TRAITS['emotional']['negative'][4], AGES['youth']),  #

            # Socialization to Interaction
            (TRAITS['socialization']['positive'][0], TRAITS['interaction']['positive'][0], AGES['youth']),  #
            (TRAITS['socialization']['positive'][1], TRAITS['interaction']['positive'][1], AGES['youth']),  #
            (TRAITS['socialization']['positive'][2], TRAITS['interaction']['positive'][2], AGES['youth']),  #
            (TRAITS['socialization']['positive'][3], TRAITS['interaction']['positive'][3], AGES['youth']),  #
            (TRAITS['socialization']['positive'][4], TRAITS['interaction']['positive'][4], AGES['youth']),  #
            (TRAITS['socialization']['neutral'][0], TRAITS['interaction']['neutral'][0], AGES['youth']),    #
            (TRAITS['socialization']['neutral'][1], TRAITS['interaction']['neutral'][1], AGES['youth']),    #
            (TRAITS['socialization']['neutral'][2], TRAITS['interaction']['neutral'][2], AGES['youth']),    #
            (TRAITS['socialization']['neutral'][3], TRAITS['interaction']['neutral'][3], AGES['youth']),    #
            (TRAITS['socialization']['neutral'][4], TRAITS['interaction']['neutral'][4], AGES['youth']),    #
            (TRAITS['socialization']['negative'][0], TRAITS['interaction']['negative'][0], AGES['youth']),  #
            (TRAITS['socialization']['negative'][1], TRAITS['interaction']['negative'][1], AGES['youth']),  #
            (TRAITS['socialization']['negative'][2], TRAITS['interaction']['negative'][2], AGES['youth']),  #
            (TRAITS['socialization']['negative'][3], TRAITS['interaction']['negative'][3], AGES['youth']),  #
            (TRAITS['socialization']['negative'][4], TRAITS['interaction']['negative'][4], AGES['youth']),  #

            # Cognition to Identity
            (TRAITS['cognition']['positive'][0], TRAITS['identity']['positive'][0], AGES['adolescent']),  #
            (TRAITS['cognition']['positive'][1], TRAITS['identity']['positive'][1], AGES['adolescent']),  #
            (TRAITS['cognition']['positive'][2], TRAITS['identity']['positive'][2], AGES['adolescent']),  #
            (TRAITS['cognition']['positive'][3], TRAITS['identity']['positive'][3], AGES['adolescent']),  #
            (TRAITS['cognition']['positive'][4], TRAITS['identity']['positive'][4], AGES['adolescent']),  #
            (TRAITS['cognition']['neutral'][0], TRAITS['identity']['neutral'][0], AGES['adolescent']),    #
            (TRAITS['cognition']['neutral'][1], TRAITS['identity']['neutral'][1], AGES['adolescent']),    #
            (TRAITS['cognition']['neutral'][2], TRAITS['identity']['neutral'][2], AGES['adolescent']),    #
            (TRAITS['cognition']['neutral'][3], TRAITS['identity']['neutral'][3], AGES['adolescent']),    #
            (TRAITS['cognition']['neutral'][4], TRAITS['identity']['neutral'][4], AGES['adolescent']),    #
            (TRAITS['cognition']['negative'][0], TRAITS['identity']['negative'][0], AGES['adolescent']),  #
            (TRAITS['cognition']['negative'][1], TRAITS['identity']['negative'][1], AGES['adolescent']),  #
            (TRAITS['cognition']['negative'][2], TRAITS['identity']['negative'][2], AGES['adolescent']),  #
            (TRAITS['cognition']['negative'][3], TRAITS['identity']['negative'][3], AGES['adolescent']),  #
            (TRAITS['cognition']['negative'][4], TRAITS['identity']['negative'][4], AGES['adolescent']),  #

            # Identity to Morals
            (TRAITS['identity']['positive'][0], TRAITS['morals']['positive'][0], AGES['mature']),  #
            (TRAITS['identity']['positive'][1], TRAITS['morals']['positive'][1], AGES['mature']),  #
            (TRAITS['identity']['positive'][2], TRAITS['morals']['positive'][2], AGES['mature']),  #
            (TRAITS['identity']['positive'][3], TRAITS['morals']['positive'][3], AGES['mature']),  #
            (TRAITS['identity']['positive'][4], TRAITS['morals']['positive'][4], AGES['mature']),  #
            (TRAITS['identity']['neutral'][0], TRAITS['morals']['neutral'][0], AGES['mature']),    #
            (TRAITS['identity']['neutral'][1], TRAITS['morals']['neutral'][1], AGES['mature']),    #
            (TRAITS['identity']['neutral'][2], TRAITS['morals']['neutral'][2], AGES['mature']),    #
            (TRAITS['identity']['neutral'][3], TRAITS['morals']['neutral'][3], AGES['mature']),    #
            (TRAITS['identity']['neutral'][4], TRAITS['morals']['neutral'][4], AGES['mature']),    #
            (TRAITS['identity']['negative'][0], TRAITS['morals']['negative'][0], AGES['mature']),  #
            (TRAITS['identity']['negative'][1], TRAITS['morals']['negative'][1], AGES['mature']),  #
            (TRAITS['identity']['negative'][2], TRAITS['morals']['negative'][2], AGES['mature']),  #
            (TRAITS['identity']['negative'][3], TRAITS['morals']['negative'][3], AGES['mature']),  #
            (TRAITS['identity']['negative'][4], TRAITS['morals']['negative'][4], AGES['mature']),  #

            # Cognition to Ambition
            (TRAITS['cognition']['positive'][2], TRAITS['ambition']['positive'][0], AGES['prime']),  #
            (TRAITS['cognition']['positive'][3], TRAITS['ambition']['positive'][1], AGES['prime']),  #
            (TRAITS['cognition']['positive'][4], TRAITS['ambition']['positive'][2], AGES['prime']),  #
            (TRAITS['cognition']['neutral'][1], TRAITS['ambition']['neutral'][0], AGES['prime']),    #
            (TRAITS['cognition']['neutral'][2], TRAITS['ambition']['neutral'][1], AGES['prime']),    #
            (TRAITS['cognition']['neutral'][3], TRAITS['ambition']['neutral'][2], AGES['prime']),    #
            (TRAITS['cognition']['negative'][1], TRAITS['ambition']['negative'][0], AGES['prime']),  #
            (TRAITS['cognition']['negative'][2], TRAITS['ambition']['negative'][1], AGES['prime']),  #
            (TRAITS['cognition']['negative'][3], TRAITS['ambition']['negative'][2], AGES['prime']),  #

            # Morals to Perspective
            (TRAITS['morals']['positive'][0], TRAITS['perspective']['positive'][0], AGES['sage']),  #
            (TRAITS['morals']['positive'][1], TRAITS['perspective']['positive'][1], AGES['sage']),  #
            (TRAITS['morals']['positive'][2], TRAITS['perspective']['positive'][2], AGES['sage']),  #
            (TRAITS['morals']['neutral'][0], TRAITS['perspective']['neutral'][0], AGES['sage']),    #
            (TRAITS['morals']['neutral'][1], TRAITS['perspective']['neutral'][1], AGES['sage']),    #
            (TRAITS['morals']['neutral'][2], TRAITS['perspective']['neutral'][2], AGES['sage']),    #
            (TRAITS['morals']['negative'][0], TRAITS['perspective']['negative'][0], AGES['sage']),  #
            (TRAITS['morals']['negative'][1], TRAITS['perspective']['negative'][1], AGES['sage']),  #
            (TRAITS['morals']['negative'][2], TRAITS['perspective']['negative'][2], AGES['sage']),  #

            # Perspective to Legacy
            (TRAITS['perspective']['positive'][0], TRAITS['legacy']['positive'][0], AGES['sage']),  #
            (TRAITS['perspective']['positive'][1], TRAITS['legacy']['positive'][1], AGES['sage']),  #
            (TRAITS['perspective']['positive'][2], TRAITS['legacy']['positive'][2], AGES['sage']),  #
            (TRAITS['perspective']['neutral'][0], TRAITS['legacy']['neutral'][0], AGES['sage']),    #
            (TRAITS['perspective']['neutral'][1], TRAITS['legacy']['neutral'][1], AGES['sage']),    #
            (TRAITS['perspective']['negative'][0], TRAITS['legacy']['negative'][0], AGES['sage']),  #
            (TRAITS['perspective']['negative'][1], TRAITS['legacy']['negative'][1], AGES['sage']),  #
            (TRAITS['perspective']['negative'][2], TRAITS['legacy']['negative'][2], AGES['sage'])
        ]

        self.synergies = [
            (('curious', 'inquisitive'), 'enhances learning speed for knowledge-seeking skills'),
            (('cheerful', 'optimistic'), 'boosts creativity-related skill gains'),
            (('friendly', 'empathetic'), 'improves social relationships and diplomacy'),
            (('diligent', 'dedicated'), 'increases productivity and work efficiency'),
            (('creative', 'innovative'), 'enhances problem-solving and critical thinking'),
            (('shy', 'reserved'), 'reduces social anxiety and improves self-confidence'),
            (('moody', 'passionate'), 'increases emotional intensity and creativity'),
            (('anxious', 'sensitive'), 'improves emotional intelligence and empathy'),
            (('pessimistic', 'cynical'), 'increases critical thinking and skepticism'),
            (('conformist', 'traditional'), 'improves social standing and reputation'),
            (('rebellious', 'nonconformist'), 'increases independence and self-reliance'),
            (('insecure', 'self-doubting'), 'improves self-awareness and personal growth'),
            (('stubborn', 'unyielding'), 'increases determination and perseverance'),
            (('uncritical', 'naive'), 'improves open-mindedness and adaptability'),
            (('distracted', 'disorganized'), 'reduces procrastination and improves time management'),
            (('manipulative', 'deceptive'), 'increases persuasion and negotiation skills'),
            (('confrontational', 'aggressive'), 'increases assertiveness and conflict resolution skills'),
            (('workaholic', 'obsessive'), 'increases productivity and work efficiency'),
            (('indecisive', 'hesitant'), 'improves decision-making and risk-taking'),
            (('materialistic', 'greedy'), 'increases wealth and material possessions'),
            (('judgmental', 'critical'), 'increases critical thinking and discernment'),
            (('hedonistic', 'self-indulgent'), 'increases pleasure and enjoyment'),
            (('cynical', 'jaded'), 'increases skepticism and critical thinking'),
            (('regretful', 'remorseful'), 'improves self-awareness and personal growth'),
            (('bitter', 'resentful'), 'increases emotional intensity and motivation'),
            (('disengaged', 'detached'), 'reduces emotional attachment and increases independence'),
            (('controlling', 'manipulative'), 'increases persuasion and negotiation skills'),
            (('resentful', 'vindictive'), 'increases motivation and drive'),
            (('mentoring', 'guiding'), 'improves leadership and teaching skills'),
            (('philanthropic', 'altruistic'), 'increases generosity and kindness'),
            (('inspiring', 'visionary'), 'increases charisma and leadership skills'),
            (('reflective', 'introspective'), 'improves self-awareness and personal growth'),
            (('private', 'reserved'), 'reduces social anxiety and improves self-confidence'),
            (('traditional', 'conservative'), 'improves social standing and reputation'),
            (('adaptable', 'easy-going'), 'enhances flexibility and stress management'),
            (('engaging', 'sociable'), 'boosts charisma and social influence'),
            (('hopeful', 'joyful'), 'increases resilience and positivity'),
            (('self-aware', 'confident'), 'enhances personal growth and self-acceptance'),
            (('goal-oriented', 'ambitious'), 'increases focus and achievement'),
            (('generous', 'compassionate'), 'strengthens community bonds and support'),
            (('pragmatic', 'flexible'), 'improves problem-solving and adaptability'),
            (('mellow', 'balanced'), 'enhances emotional stability and calmness'),
            (('reflective', 'philosophical'), 'deepens understanding and wisdom'),
            (('authentic', 'principled'), 'promotes integrity and trustworthiness')
        ]

# Example of how to use the Traits class
traits_instance = Traits()
print(traits_instance.traits)
print(traits_instance.evolutions)
print(traits_instance.synergies)