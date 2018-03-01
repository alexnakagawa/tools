class Subject:
    '''
    A Subject object keeps track of all data for a person's whole experiment.
    Each Subject should have 3 Variations saved in a dictionary.
    '''

    def __init__(self, first_name, last_name, user_id='00'):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.variations = {}
        self.variation_count = 1 # max 3

    def __repr__(self):
        return 'Subject() object'

    def __str__(self):
        return 'Full Name: %s \n ID: ' % (name, user_id)

    def new_variation(self):
        '''
        Append a new variation, raise error if too many variations
        return: None
        '''
        if ((self.variation_count < 1) or (self.variation_count > 5)):
            self.variation_count = 1
            raise VariationError('Oh no, the variation did not reset correctly.')
        self.variations[step] = Variation(self.variation_count)
        if (self.variation_count == 5):
            self.variation_count = 1
            return
        self.variation_count += 1


class Variation:
    '''
    Variation should keep track the different parts of the current experiment.
    Each variation will also have an object attached to it.
    '''

    def __init__(self, step=1):
        self.step = step
        self.trials = {}
        self.trial_count = 1 # max 5

    def __repr__(self):
        return 'Variation() object'

    def __str__(self):
        return 'Variation #%d \n Completed Trials: ' % (step, len(trials))

    def new_trial(self):
        if (self.trial_count < 0 or self.trial_count > 5):
            raise TrialError('Oh no, the trial did not reset correctly.')
        self.trials[trial_number] = Trial()


class Trial:
    ''' 
    Trial class handles the iteration of a variation
    with the same attributes each time.
    '''

    def __init__(self, step=1):
        self.step = step
        self.trials = {}
        self.trial_count = 1 # max 5

    def __repr__(self):
        return 'Variation() object'

    def __str__(self):
        return 'Trial #%d \n Completed Trials: ' % (step, len(trials))

# class Object:




# def spacebar_instructions(surface, font_type):
#     ''' 
#     Render the spacebar instructions on specified surface
#     return: None
#     '''
#     title = font_type.render("Press the [spacebar] to continue", 1, BLACK)
#     title = title.convert()
#     titlepos = title.get_rect()
#     titlepos.centerx = surface.get_rect().centerx
