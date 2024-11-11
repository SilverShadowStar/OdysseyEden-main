
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

# Genes
SEX: List[str] = ['X', 'Y']
GENDER: List[str] = ['masc', 'fem', 'androgynous']
TONE: List[str] = ['pale', 'medium', 'tan', 'dark', 'deep']
UNDERTONE: List[str] = ['warm', 'neutral', 'cool']
HEIGHT: List[str] = ['short', 'average', 'tall']
BSHAPE: List[str] = ['slim', 'average', 'athletic', 'curvy']
BSIZE: List[str] = ['small', 'medium', 'large']
HCOLOR: List[str] = ['black', 'brown', 'blonde', 'ginger']
HTEXT: List[str] = ['straight', 'wavy', 'curly']
ESHAPE: List[str] = ['round', 'almond', 'upturned', 'downturned', 'hooded']
ECOLOR: List[str] = ['brown', 'hazel', 'green', 'blue', 'grey']
NPROFILE: List[str] = ['small', 'medium', 'tall']
NSHAPE: List[str] = ['refined', 'hero', 'soft', 'perky', 'dainty', 'strong', 'bulb']
MSHAPE: List[str] = ['thin', 'round', 'wide', 'fuller lower', 'fuller upper', 'downturned', 'bowshaped', 'full', 'heartshaped']
RSHAPE: List[str] = ['round', 'pointed']
RSIZE: List[str] = ['small', 'medium', 'large']

GENE_TYPES: Dict[str, List[str]] = {
    'sex': SEX,
    'gender': GENDER,
    'tone': TONE,
    'undertone': UNDERTONE,
    'height': HEIGHT,
    'bshape': BSHAPE,
    'bsize': BSIZE,
    'hcolor': HCOLOR,
    'htext': HTEXT,
    'eshape': ESHAPE,
    'ecolor': ECOLOR,
    'nprofile': NPROFILE,
    'nshape': NSHAPE,
    'mshape': MSHAPE,
    'rshape': RSHAPE,
    'rsize': RSIZE
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

TRAIT_EVOLUTIONS = [
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

TRAIT_SYNERGIES = [
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

CORE_STATS={
    'stamina': int,
    'strength': int,
    'dexterity': int,
    'perception': int,
    'willpower': int},
ADVANCED_STATS={
    'endurance': int,
    'prowess': int,
    'finesse': int,
    'conviction': int,
    'vitality': int}

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
