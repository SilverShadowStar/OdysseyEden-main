
# constants.py

class AssetPath:
	PLAYER_SPRITE = 
	CLOTHING_SPRITE = 
	WALL_SPRITE = 
	TILE_SPRITE = 
	ANIMAL_SPRITE = 
	TOOL_SPRITE = 
	PLANT_SPRITE = 
	FOOD_SPRITE = 
	ROCK_SPRITE = 
	COLLECTABLE_SPRITE = 
	FSX_SPRITE = 
	
#Window
class Window:
	def __init__(self):
		self.DEVICE_WIDTH = pygame.display.Info().current_w
		self.DEVICE_HEIGHT = pygame.display.Info().current_h
		self.DESIGN_WIDTH = 1080
		self.DESIGN_HEIGHT = 1920
		self.SCALE_X = self.DEVICE_WIDTH / self.DESIGN_WIDTH
		self.SCALE_Y = self.DEVICE_HEIGHT / self.DESIGN_HEIGHT
		self.FPS = 60

	def scale_position(self, x, y):
		return(x  * self.SCALE_X , y * self.SCALE_Y)

	def scale_size(self, width, height):
		return()

#Time
HOUR_LEN = 60
DAY_LEN = 24
WEEK_LEN = 10
MONTH_LEN = 30
YEAR_LEN = 10

MORNING = [6, 7, 8, 9, 10, 11]
AFTERNOON = [12, 13, 14, 15, 16]
EVENING = [17, 18, 19, 20, 21, 22]
NIGHT = [23, 24, 1, 2, 3, 4, 5]

MONTH_NAMES = ['Brigide', 'Imbolka', 'Floralis', 'Lithara',
               'Heliax', 'Aestium', 'Mabonel', 'Ceresio', 'Yulith', 'Hibernis']
DAY_NAMES = ['Restony', 'Serement', 'Chronesis', 'Tempetude', 'Solament',
             'Helioris', 'Duratonis', 'Resporal', 'Sabbathal', 'Noctitude']

AGES = {
    'infant': (0, 2),
    'sprout': (3, 4),
    'youth': (5, 12),
    'adolescent': (13, 17),
    'prime': (18, 29),
    'mature': (30, 59),
    'sage': (60, 120)
}

class Traits:
    temperament={
        'name': 'temperament',
        'positive': [
            'easy-going',
            'adaptable',
            'content',
            'cheerful',
            'calm'
        ],
        'neutral': [
            'active',
            'regular',
            'slow-to-warm-up',
            'moderate',
            'observant'
        ],
        'negative': [
            'fussy',
            'irritable',
            'unpredictable',
            'restless',
            'overactive'
        ]
    },
    socialization={
        'name': 'socialization',
        'positive': [
            'sociable',
            'playful',
            'affectionate',
            'friendly',
            'outgoing'
        ],
        'neutral': [
            'observant',
            'independent',
            'cautious',
            'curious',
            'mellow'
        ],
        'negative': [
            'clingy',
            'irritable',
            'withdrawn',
            'hyperactive',
            'impulsive'
        ]
    },
    emotional={
    'name': 'emotional',
        'positive': [
            'cheerful',
            'passionate',
            'optimistic',
            'joyful',
            'hopeful'
        ],
        'neutral': [
            'sensitive',
            'calm',
            'reflective',
            'balanced',
            'realistic'
        ],
        'negative': [
            'moody',
            'anxious',
            'gloomy',
            'aggressive',
            'doubtful'
        ]
    },
    interaction={
    'name': 'interaction',
        'positive': [
            'cooperative',
            'empathetic',
            'supportive',
            'generous',
            'trustworthy'
        ],
        'neutral': [
            'reserved',
            'independent',
            'adaptable',
            'neutral',
            'pragmatic'
        ],
        'negative': [
            'shy',
            'confrontational',
            'manipulative',
            'aloof',
            'dismissive'
        ]
    },
    cognition={
    'name': 'cognition',
        'positive': [
            'curious',
            'diligent',
            'creative',
            'inquisitive',
            'motivated'
        ],
        'neutral': [
            'practical',
            'analytical',
            'intuitive',
            'theoretical',
            'exploratory'
        ],
        'negative': [
            'distracted',
            'stubborn',
            'uncritical',
            'complacent',
            'disinterested'
        ]
    },
    identity={
    'name': 'identity',
        'positive': [
            'confident',
            'principled',
            'open-minded',
            'self-aware',
            'authentic'
        ],
        'neutral': [
            'questioning',
            'experimental',
            'idealistic',
            'reflective',
            'curious'
        ],
        'negative': [
            'insecure',
            'conformist',
            'rebellious',
            'conflicted',
            'doubtful'
        ]
    },
    ambition={
    'name': 'ambition',
        'positive': [
            'ambitious',
            'dedicated',
            'innovative',
            'goal-oriented',
            'driven'
        ],
        'neutral': [
            'flexible',
            'specialized',
            'risk-taking',
            'pragmatic',
            'adaptable'
        ],
        'negative': [
            'unmotivated',
            'workaholic',
            'indecisive',
            'complacent',
            'disengaged'
        ]
    },
    morals={
    'name': 'morals',
        'positive': [
            'honest',
            'compassionate',
            'resilient',
            'fair-minded',
            'generous'
        ],
        'neutral': [
            'traditional',
            'pragmatic',
            'individualistic',
            'balanced',
            'neutral'
        ],
        'negative': [
            'materialistic',
            'judgmental',
            'hedonistic',
            'selfish',
            'cynical'
        ]
    },
    perspective={
    'name': 'perspective',
        'positive': [
            'wise',
            'content',
            'grateful',
            'optimistic',
            'hopeful'
        ],
        'neutral': [
            'philosophical',
            'nostalgic',
            'accepting',
            'realistic',
            'pragmatic'
        ],
        'negative': [
            'cynical',
            'regretful',
            'bitter',
            'despondent',
            'resentful'
        ]
    },
    legacy={
    'name': 'legacy',
        'positive': [
            'mentoring',
            'philanthropic',
            'inspiring',
            'guiding',
            'visionary'
        ],
        'neutral': [
            'reflective',
            'private',
            'traditional',
            'conservative',
            'practical'
        ],
        'negative': [
            'disengaged',
            'controlling',
            'resentful',
            'manipulative',
            'detached'
        ]
    }


class Stats:
    core={
        'stamina': int,
        'strength': int,
        'dexterity': int,
        'perception': int,
        'willpower': int},
    advanced={
        'endurance': int,
        'prowess': int,
        'finess': int,
        'conviction': int,
        'vitality': int}


class skills:
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
}

#Possible responses from ai
class responses:
    def __init__(self) -> None:
        pass
    ['receptive', 'motive', 'apprehensive', 'refusal']
