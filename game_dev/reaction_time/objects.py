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
        if self.variation_count > 3:
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

    def get_attributes(self):
        return self.attributes

    def new_trial(self):
        if self.trial_count > 5:
            raise ValueError('Oh no, something went wrong...')
        self.trials[self.trial_count] = Trial(self.trial_count)
        self.trial_count += 1


class Trial:
    """ 
    Trial class handles the iteration of a variation
    with the same attributes each time.
    """

    def __init__(self, step=1):
        self.step = step
        self.trial_count = 1  # max 5
        self.delay_time = 1000.0  # in ms
        self.reaction_time = 0.0  # in ms
        self.x_pos = 0
        self.y_pos = 0

    def __repr__(self):
        return 'Trial() object'

    def __str__(self):
        return 'Trial #%d' % self.trial_count

    def set_delay_time(self, delay_time):
        """
        Delay time is some time between 1000 ms (1.0 sec) to 5000 ms (5.0 sec)
        """
        self.delay_time = delay_time
        return

    def set_reaction_time(self, reaction_time):
        self.reaction_time = reaction_time
        return

    def set_x_pos(self, x_pos):
        self.x_pos = x_pos
        return

    def set_y_pos(self, y_pos):
        self.y_pos = y_pos
        return