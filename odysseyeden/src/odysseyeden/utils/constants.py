
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
WEEK_LEN = 5
MONTH_LEN = 30
YEAR_LEN = 5

MORNING = [6, 7, 8, 9, 10, 11]
AFTERNOON = [12, 13, 14, 15, 16]
EVENING = [17, 18, 19, 20, 21, 22]
NIGHT = [23, 24, 1, 2, 3, 4, 5]

MONTH_NAMES = ['Brigide', 'Floralis', 'Heliax', 'Aestium', 'Ceresio']
DAY_NAMES = ['Serement', 'Chronesis', 'Solament', 'Resporal', 'Noctitude']

AGES = {
    'infant': (0, 2),
    'sprout': (3, 4),
    'youth': (5, 12),
    'adolescent': (13, 17),
    'prime': (18, 29),
    'mature': (30, 59),
    'sage': (60, 120)
}
TRAITS = ['easy-going',
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
            


"""class Traits:
    temperament={
        'name': 'temperament',
        'positive': [
            TRAITS[0],
            TRAITS[1],
            TRAITS[2],
            TRAITS[3],
            TRAITS[4]

        ],
        'neutral': [
            TRAITS[5],
            TRAITS[6],
            TRAITS[7],
            TRAITS[8],
            TRAITS[9]
        ],
        'negative': [
            TRAITS[10],
            TRAITS[11],
            TRAITS[12],
            TRAITS[13],
            TRAITS[14]
        ]
    },
    socialization={
        'name': 'socialization',
        'positive': [
            TRAITS[15],
            TRAITS[16],
            TRAITS[17],
            TRAITS[18],
            TRAITS[19]
        ],
        'neutral': [
            TRAITS[20],
            TRAITS[21],
            TRAITS[22],
            TRAITS[23],
            TRAITS[24]
        ],
        'negative': [
            TRAITS[25],
            TRAITS[26],
            TRAITS[27],
            TRAITS[28],
            TRAITS[29]
        ]
    },
    emotional={
    'name': 'emotional',
        'positive': [
            TRAITS[30],
            TRAITS[31],
            TRAITS[32],
            TRAITS[33],
            TRAITS[34]
        ],
        'neutral': [
            TRAITS[35],
            TRAITS[36],
            TRAITS[37],
            TRAITS[38],
            TRAITS[39]
        ],
        'negative': [
            TRAITS[40],
            TRAITS[41],
            TRAITS[42],
            TRAITS[43],
            TRAITS[44]
        ]
    },
    interaction={
    'name': 'interaction',
        'positive': [
            TRAITS[45],
            TRAITS[46],
            TRAITS[47],
            TRAITS[48],
            TRAITS[49]
        ],
        'neutral': [
            TRAITS[50],
            TRAITS[51],
            TRAITS[52],
            TRAITS[53],
            TRAITS[54]
        ],
        'negative': [
            TRAITS[55],
            TRAITS[56],
            TRAITS[57],
            TRAITS[58],
            TRAITS[59]
        ]
    },
    cognition={
    'name': 'cognition',
        'positive': [
            TRAITS[60],
            TRAITS[61],
            TRAITS[62],
            TRAITS[63],
            TRAITS[64]
        ],
        'neutral': [
            TRAITS[65],
            TRAITS[66],
            TRAITS[67],
            TRAITS[68],
            TRAITS[69]
        ],
        'negative': [
            TRAITS[70],
            TRAITS[71],
            TRAITS[72],
            TRAITS[73],
            TRAITS[74]
        ]
    },
    identity={
    'name': 'identity',
        'positive': [
            TRAITS[75],
            TRAITS[76],
            TRAITS[77],
            TRAITS[78],
            TRAITS[79]
        ],
        'neutral': [
            TRAITS[80],
            TRAITS[81],
            TRAITS[82],
            TRAITS[83],
            TRAITS[84]
        ],
        'negative': [
            TRAITS[85],
            TRAITS[86],
            TRAITS[87],
            TRAITS[88],
            TRAITS[89]
        ]
    },
    ambition={
    'name': 'ambition',
        'positive': [
            TRAITS[90],
            TRAITS[91],
            TRAITS[92],
            TRAITS[93],
            TRAITS[94]
        ],
        'neutral': [
            TRAITS[95],
            TRAITS[96],
            TRAITS[97],
            TRAITS[98],
            TRAITS[99]
        ],
        'negative': [
            TRAITS[100],
            TRAITS[101],
            TRAITS[102],
            TRAITS[103],
            TRAITS[104]
        ]
    },
    morals={
    'name': 'morals',
        'positive': [
            TRAITS[105],
            TRAITS[106],
            TRAITS[107],
            TRAITS[108],
            TRAITS[109]
        ],
        'neutral': [
            TRAITS[110],
            TRAITS[111],
            TRAITS[112],
            TRAITS[113],
            TRAITS[114]
        ],
        'negative': [
            TRAITS[115],
            TRAITS[116],
            TRAITS[117],
            TRAITS[118],
            TRAITS[119]
        ]
    },
    perspective={
    'name': 'perspective',
        'positive': [
            TRAITS[120],
            TRAITS[121],
            TRAITS[122],
            TRAITS[123],
            TRAITS[124]
        ],
        'neutral': [
            TRAITS[125],
            TRAITS[126],
            TRAITS[127],
            TRAITS[128],
            TRAITS[129]
        ],
        'negative': [
            TRAITS[130],
            TRAITS[131],
            TRAITS[132],
            TRAITS[133],
            TRAITS[134]
        ]
    },
    legacy={
    'name': 'legacy',
        'positive': [
            TRAITS[135],
            TRAITS[136],
            TRAITS[137],
            TRAITS[138],
            TRAITS[139]
        ],
        'neutral': [
            TRAITS[140],
            TRAITS[141],
            TRAITS[142],
            TRAITS[143],
            TRAITS[144]
        ],
        'negative': [
            TRAITS[145],
            TRAITS[146],
            TRAITS[147],
            TRAITS[148],
            TRAITS[149]
        ]
    }
""" 

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
