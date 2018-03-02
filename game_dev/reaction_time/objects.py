# Colors
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

# Dictionary mappings to object attributes
SHAPE_DICT = {1: 'Circle', 2: 'Triangle'}
COLOR_DICT = {1: RED, 2: PURPLE}
MUSIC_DICT = {1: '', 2: '', 3: ''}


class Subject:
    """
    A Subject object keeps track of all data for a person's whole experiment.
    Each Subject should have 3 Variations saved in a dictionary.
    """

    def __init__(self, user_id, first_name, last_name):
        if len(user_id) != 2:
            raise ValueError('user_id should be 2 chars long. Please input valid id.')
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.variations = {}
        self.variation_count = 1  # max 3

    def __repr__(self):
        return 'Subject() object'

    def __str__(self):
        return 'Full Name: %s %s\nID: %s' % (self.first_name, self.last_name, self.user_id)

    def get_name(self):
        return self.first_name, self.last_name

    def get_id(self):
        return self.user_id

    def display_variations(self):
        return self.variations 

    def new_variation(self):
        """
        Append a new variation, raise error if too many variations
        return: None
        """
        if self.variation_count < 1 or self.variation_count > 3:
            self.variation_count = 1
            raise ValueError('Oh no, you cannot have more than 3.')
        # Change attributes later
        temp = Variation(self.variation_count)
        self.variations[self.variation_count] = temp
        self.variation_count += 1
        return 


class Variation:
    """
    Variation should keep track the different parts of the current experiment.
    Each variation will also have an object attached to it.
    Each variation will have 5 trials
    """

    def __init__(self, step, shape=1, color=1, music=1):
        self.step = step
        self.trials = {}
        self.trial_count = 1  # max 5
        self.Object = None
        self.shape = shape
        self.color = color
        self.music = music
        self.attributes = [shape, color, music]

    def __repr__(self):
        return 'Variation %s: %s, %s, %s' % (self.step, self.shape, self.color, self.music)

    def __str__(self):
        return 'Variation #%d of Subject\n \
                Attributes of variation: %s\n \
                Completed Trials: %d' % (self.step, self.attributes, len(self.trials))

    def new_trial(self):
        if self.trial_count < 0 or self.trial_count > 5:
            self.trial_count = 1
            raise ValueError('Oh no, the trial did not reset correctly. Resetting to 1...')
        self.trials[self.trial_count] = Trial(self.trial_count)

    def new_object(self):
        self.Object = Object(self.attributes)


class Trial:
    """ 
    Trial class handles the iteration of a variation
    with the same attributes each time.
    """

    def __init__(self, step=1):
        self.step = step
        self.trial_count = 1  # max 5
        self.delay_time = 1000.0  # in ms

    def __repr__(self):
        return 'Trial() object'

    def __str__(self):
        return 'Trial #%d' % self.trial_count

    def set_delay_time(self, delay_time):
        """
        Delay time is some time between 1000 ms (1.0 sec) to 7000 ms ()
        """
        self.delay_time = delay_time
        return delay_time


class Object:
    """
    location:
    color:
    shape:
    music:
    """

    # TODO
    def __init__(self, attributes):
        if len(attributes) != 3:
            raise ValueError('Attributes list should be 3 ints')
        self.color = attributes[0]
        self.shape = attributes[1]
        self.music = attributes[2]

    def __repr__(self):
        return 'Object() object'

    def __str__(self):
        return 'Color: %s\nShape: %s\nMusic: %s\n' % (self.color, self.shape, self.music)
