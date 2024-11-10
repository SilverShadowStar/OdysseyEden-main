import random
class Genes:
    SEX = ['x', 'y']
    GENDER = ['masc', 'fem', 'androgynous']
    TONE = ['pale', 'medium', 'tan', 'dark', 'deep']
    UNDERTONE = ['warm', 'neutral', 'cool']
    HEIGHT = ['short', 'average', 'tall']
    BSHAPE = ['slim', 'average', 'athletic', 'curvy']
    BSIZE = ['small', 'medium', 'large']
    HCOLOR = ['black', 'brown', 'blonde', 'ginger']
    HTEXT = ['straight', 'wavy', 'curly']
    ESHAPE = ['round', 'almond', 'upturned', 'downturned', 'hooded']
    ECOLOR = ['brown', 'hazel', 'green', 'blue', 'grey']
    NPROFILE = ['small', 'medium', 'tall']
    NSHAPE = ['refined', 'hero', 'soft', 'perky', 'dainty', 'strong', 'bulb']
    MSHAPE = ['thin', 'round', 'wide', 'fuller lower', 'fuller upper', 'downturned', 'bowshaped', 'full', 'heartshaped']
    RSHAPE = ['round', 'pointed']
    RSIZE = ['small', 'medium', 'large']

class DNA:
    def __init__(self, **kwargs):
        """
        Initialize a DNA object.

        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'sex1': A string indicating the first sex of the character (one of 'x' or 'y').
            - 'sex2': A string indicating the second sex of the character (one of 'x' or 'y').
            - 'gender1': A string indicating the gender of the character (one of 'masc', 'fem', or 'androgynous').
            - 'gender2': A string indicating the secondary gender of the character (one of 'masc', 'fem', or 'androgynous').
            - 'skin1': A string indicating the skin tone of the first parent (one of 'pale', 'medium', 'tan', or 'dark').
            - 'skin2': A string indicating the skin tone of the second parent (one of 'pale', 'medium', 'tan', or 'dark').
            - 'height1': A string indicating the height of the first parent (one of 'short', 'average', or 'tall').
            - 'height2': A string indicating the height of the second parent (one of 'short', 'average', or 'tall').
            - 'body1': A string indicating the body shape of the first parent (one of 'slim', 'average', 'athletic', or 'curvy').
            - 'body2': A string indicating the body shape of the second parent (one of 'slim', 'average', 'athletic', or 'curvy').
            - 'hair1': A string indicating the hair color of the first parent (one of 'black', 'brown', 'blonde', 'ginger').
            - 'hair2': A string indicating the hair color of the second parent (one of 'black', 'brown', 'blonde', 'ginger').
            - 'eyes1': A string indicating the eye shape of the first parent (one of 'round', 'almond', 'upturned', or 'downturned').
            - 'eyes2': A string indicating the eye shape of the second parent (one of 'round', 'almond', 'upturned', or 'downturned').
            - 'nose1': A string indicating the nose profile of the first parent (one of 'small', 'medium', or 'tall').
            - 'nose2': A string indicating the nose profile of the second parent (one of 'small', 'medium', or 'tall').
            - 'mouth1': A string indicating the mouth shape of the first parent (one of 'thin', 'round', 'wide', 'fuller lower', 'fuller upper', 'downturned', 'bowshaped', 'full', 'heartshaped').
            - 'mouth2': A string indicating the mouth shape of the second parent (one of 'thin', 'round', 'wide', 'fuller lower', 'fuller upper', 'downturned', 'bowshaped', 'full', 'heartshaped').
            - 'ears1': A string indicating the ear shape of the first parent (one of 'round', 'pointed').
            - 'ears2': A string indicating the ear shape of the second parent (one of 'round', 'pointed').
        """
        self.gender = self._generate_gender(**kwargs)
        self.skin = self._generate_skin(**kwargs)
        self.height = self._generate_height(**kwargs)
        self.body = self._generate_body(**kwargs)
        self.hair = self._generate_hair(**kwargs)
        self.eyes = self._generate_eyes(**kwargs)
        self.nose = self._generate_nose(**kwargs)
        self.mouth = self._generate_mouth(**kwargs)
        self.ears = self._generate_ears(**kwargs)

    def _generate_gender(self, **kwargs):
        """
        Generate gender attributes for a character.
    
        This function generates the primary and secondary sex and gender attributes
        for a character using the provided keyword arguments or random defaults.
    
        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'sex1': A string indicating the first sex of the character.
            - 'sex2': A string indicating the second sex of the character.
            - 'gender1': A string indicating the gender of the character.
            - 'gender2': A string indicating the secondary gender of the character.
    
        Returns:
        - dict: A dictionary containing 'sex1', 'sex2', 'gender1', and 'gender2' keys
          with their respective values.
        """
        return {
            'sex1': kwargs.get('sex1', Genes.SEX[0]),
            'sex2': kwargs.get('sex2', random.choice(Genes.SEX)),
            'gender1': kwargs.get('gender1', random.choice(Genes.GENDER)),
            'gender2': kwargs.get('gender2', random.choice(Genes.GENDER))
        }

    def _generate_skin(self, **kwargs):
        """
        Generate skin attributes for a character.

        This function generates the tone and undertone for each of the two parents
        of a character using the provided keyword arguments or random defaults.

        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'tone1': A string indicating the skin tone of the first parent.
            - 'tone2': A string indicating the skin tone of the second parent.
            - 'undertone1': A string indicating the skin undertone of the first parent.
            - 'undertone2': A string indicating the skin undertone of the second parent.

        Returns:
        - dict: A dictionary containing 'tone1', 'tone2', 'undertone1', and 'undertone2' keys
          with their respective values.
        """
        return {
            'tone1': kwargs.get('tone1', random.choice(Genes.TONE)),
            'tone2': kwargs.get('tone2', random.choice(Genes.TONE)),
            'undertone1': kwargs.get('undertone1', random.choice(Genes.UNDERTONE)),
            'undertone2': kwargs.get('undertone2', random.choice(Genes.UNDERTONE))
        }

    def _generate_height(self, **kwargs):
        """
        Generate height attributes for a character.
        
        This function generates the height value and proportion for each of the two parents
        of a character using the provided keyword arguments or random defaults.
        
        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'value1': A float indicating the height value of the first parent.
            - 'value2': A float indicating the height value of the second parent.
            - 'proportion1': A string indicating the height proportion of the first parent.
            - 'proportion2': A string indicating the height proportion of the second parent.
        
        Returns:
        - dict: A dictionary containing 'value1', 'value2', 'proportion1', and 'proportion2' keys
          with their respective values.
        """
        return {
            'value1': kwargs.get('value1', random.uniform(0.8, 1.2)),
            'value2': kwargs.get('value2', random.uniform(0.8, 1.2)),
            'proportion1': kwargs.get('proportion1', random.choice(Genes.HEIGHT)),
            'proportion2': kwargs.get('proportion2', random.choice(Genes.HEIGHT))
        }

    def _generate_body(self, **kwargs):
        """
        Generate body attributes for a character.

        This function generates the body shape and size for each of the two parents
        of a character using the provided keyword arguments or random defaults.

        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'shape1': A string indicating the body shape of the first parent.
            - 'shape2': A string indicating the body shape of the second parent.
            - 'size1': A string indicating the body size of the first parent.
            - 'size2': A string indicating the body size of the second parent.

        Returns:
        - dict: A dictionary containing 'shape1', 'shape2', 'size1', and 'size2' keys
          with their respective values.
        """
        return {
            'shape1': kwargs.get('shape1', random.choice(Genes.BSHAPE)),
            'shape2': kwargs.get('shape2', random.choice(Genes.BSHAPE)),
            'size1': kwargs.get('size1', random.choice(Genes.BSIZE)),
            'size2': kwargs.get('size2', random.choice(Genes.BSIZE))
        }

    def _generate_hair(self, **kwargs):
        """
        Generate hair attributes for a character.

        This function generates the hair color and texture for each of the two parents
        of a character using the provided keyword arguments or random defaults.

        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'hair1': A string indicating the hair color of the first parent.
            - 'hair2': A string indicating the hair color of the second parent.
            - 'texture1': A string indicating the hair texture of the first parent.
            - 'texture2': A string indicating the hair texture of the second parent.

        Returns:
        - dict: A dictionary containing 'hair1', 'hair2', 'texture1', and 'texture2' keys
          with their respective values.
        """
        return {
            'hair1': kwargs.get('hair1', random.choice(Genes.HCOLOR)),
            'hair2': kwargs.get('hair2', random.choice(Genes.HCOLOR)),
            'texture1': kwargs.get('texture1', random.choice(Genes.HTEXT)),
            'texture2': kwargs.get('texture2', random.choice(Genes.HTEXT))
        }

    def _generate_eyes(self, **kwargs):
        """
        Generate eye attributes for a character.
    
        This function generates the eye shape and color for each of the two parents
        of a character using the provided keyword arguments or random defaults.
    
        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'eyes1': A string indicating the eye shape of the first parent.
            - 'eyes2': A string indicating the eye shape of the second parent.
            - 'color1': A string indicating the eye color of the first parent.
            - 'color2': A string indicating the eye color of the second parent.
    
        Returns:
        - dict: A dictionary containing 'eyes1', 'eyes2', 'color1', and 'color2' keys
          with their respective values.
        """
        return {
            'eyes1': kwargs.get('eyes1', random.choice(Genes.ESHAPE)),
            'eyes2': kwargs.get('eyes2', random.choice(Genes.ESHAPE)),
            'color1': kwargs.get('color1', random.choice(Genes.ECOLOR)),
            'color2': kwargs.get('color2', random.choice(Genes.ECOLOR))
        }

    def _generate_nose(self, **kwargs):
        """
        Generate nose attributes for a character.

        This function generates the nose profile and shape for each of the two parents
        of a character using the provided keyword arguments or random defaults.

        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'profile1': A string indicating the nose profile of the first parent.
            - 'profile2': A string indicating the nose profile of the second parent.
            - 'nose1': A string indicating the nose shape of the first parent.
            - 'nose2': A string indicating the nose shape of the second parent.

        Returns:
        - dict: A dictionary containing 'profile1', 'profile2', 'nose1', and 'nose2' keys
          with their respective values.
        """
        return {
            'profile1': kwargs.get('profile1', random.choice(Genes.NPROFILE)),
            'profile2': kwargs.get('profile2', random.choice(Genes.NPROFILE)),
            'nose1': kwargs.get('nose1', random.choice(Genes.NSHAPE)),
            'nose2': kwargs.get('nose2', random.choice(Genes.NSHAPE))
        }

    def _generate_mouth(self, **kwargs):
        """
        Generate mouth attributes for a character.

        This function generates the mouth shape for each of the two parents
        of a character using the provided keyword arguments or random defaults.

        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'mouth1': A string indicating the mouth shape of the first parent.
            - 'mouth2': A string indicating the mouth shape of the second parent.

        Returns:
        - dict: A dictionary containing 'mouth1' and 'mouth2' keys with their respective values.
        """
        return {
            'mouth1': kwargs.get('mouth1', random.choice(Genes.MSHAPE)),
            'mouth2': kwargs.get('mouth2', random.choice(Genes.MSHAPE))
        }

    def _generate_ears(self, **kwargs):
        """
        Generate ear attributes for a character.

        This function generates the ear shape and size for each of the two parents
        of a character using the provided keyword arguments or random defaults.

        Parameters:
        - **kwargs: A dictionary of keyword arguments. The recognized arguments are:
            - 'ear1': A string indicating the ear shape of the first parent.
            - 'ear2': A string indicating the ear shape of the second parent.
            - 'earsize1': A string indicating the ear size of the first parent.
            - 'earsize2': A string indicating the ear size of the second parent.

        Returns:
        - dict: A dictionary containing 'ear1', 'ear2', 'earsize1', and 'earsize2' keys
          with their respective values.
        """
        return {
            'ear1': kwargs.get('ear1', random.choice(Genes.RSHAPE)),
            'ear2': kwargs.get('ear2', random.choice(Genes.RSHAPE)),
            'earsize1': kwargs.get('earsize1', random.choice(Genes.RSIZE)),
            'earsize2': kwargs.get('earsize2', random.choice(Genes.RSIZE))
        }

    def __repr__(self):
        """
        Return a string representation of the DNA object.

        This representation is useful for debugging and testing.
        """
        return (f"DNA(gender={self.gender}, skin={self.skin}, height={self.height}, "
                f"body={self.body}, hair={self.hair}, eyes={self.eyes}, nose={self.nose}, "
                f"mouth={self.mouth}, ears={self.ears})")

    def __add__(self, other):
        """
        Combine two DNA objects.

        This method creates a new DNA object by randomly combining the attributes of the two
        input DNA objects. The new object is returned.

        Parameters:
        - other: Another DNA object to combine with.

        Raises:
        - TypeError: If the other object is not a DNA object.

        Returns:
        - DNA: A new DNA object with combined attributes.
        """
        if not isinstance(other, DNA):
            raise TypeError("Cannot combine DNA with non-DNA")

    def combine_attributes(attr1, attr2):
            return {
                key: random.choice([attr1[key], attr2[key]])
                for key in attr1.keys()
            }

        new_DNA = DNA(
            sex1=self.gender['sex1'],
            sex2=other.gender['sex2'],
            gender1=self.gender['gender1'],
            gender2=other.gender['gender2'],
            tone1=self.skin['tone1'],
            tone2=other.skin['tone2'],
            undertone1=self.skin['undertone1'],
            undertone2=other.skin['undertone2'],
            value1=self.height['value1'],
            value2=other.height['value2'],
            proportion1=self.height['proportion1'],
            proportion2=other.height['proportion2'],
            body1=self.body['body1'],
            body2=other.body['body2'],
            size1=self.body['size1'],
            size2=other.body['size2'],
            hair1=self.hair['hair1'],
            hair2=other.hair['hair2'],
            texture1=self.hair['texture1'],
            texture2=other.hair['texture2'],
            eyes1=self.eyes['eyes1'],
            eyes2=other.eyes['eyes2'],
            color1=self.eyes['color1'],
            color2=other.eyes['color2'],
            profile1=self.nose['profile1'],
            profile2=other.nose['profile2'],
            nose1=self.nose['nose1'],
            nose2=other.nose['nose2'],
            mouth1=self.mouth['mouth1'],
            mouth2=other.mouth['mouth2'],
            ears1=self.ears['ears1'],
            ears2=other.ears['ears2'],
            earsize1=self.ears['earsize1'],
            earsize2=other.ears['earsize2']
        )

    return new_DNA
