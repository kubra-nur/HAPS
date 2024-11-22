from otree.api import*

class C(BaseConstants):
    NAME_IN_URL = 'prequestionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        label='What is your age?',
        min=18,
        max=65,
        error_messages={
            'min_value': 'Please enter an age of at least 18.',
            'max_value': 'Please enter an age of 65 or less.',
            'invalid': 'Please enter a valid age between 18 and 65.',
        }
    )

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Transgender', 'Transgender'], ['Non-binary', 'Non-binary'],
                 ['Prefer not to say', 'Prefer not to say']],
        label='Which gender do you identify with?',
        widget=widgets.RadioSelect)

    field_of_study = models.StringField(
        choices=[
            ['Economics', 'Economics'],
            ['Engineering, Science, Mathematics, Information Systems or Computer Science',
             'Engineering, Science, Mathematics, Information Systems or Computer Science'],
            ['Natural Science (e.g. Physics, Biology etc.)', 'Natural Science (e.g. Physics, Biology etc.)'],
            ['Humanities, Social Sciences or Psychology', 'Humanities, Social Sciences or Psychology'],
            ['Others', 'Others']
        ],
        label='What is your field of study?',
        widget=widgets.RadioSelect
    )

    prior_experience = models.IntegerField(
        choices=[
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6']
        ],
        label='Please rate your prior experience in video meeting systems: '
              'On a scale from 1 (Novice) to 6 (Expert) ',
        widget=widgets.RadioSelectHorizontal
    )

    frequency_of_usage = models.StringField(
        choices=[
            ['At least 1 day in a week', 'At least 1 day in a week'],
            ['At least 2 days in a week', 'At least 2 days in a week'],
            ['At least 3 days in a week', 'At least 3 days in a week'],
            ['At least 4 days in a week', 'At least 4 days in a week'],
            ['5 days in a week or more', '5 days in a week or more']
        ],
        label='Please indicate your frequency of usage of video meetings in an average week',
        widget=widgets.RadioSelect
    )



    availability_to_participate = models.LongStringField(
        label='Please write down your available timeslots slots to participate in the lab study (e.g., Monday Morning, Tuesday Afternoon, etc.). Please indicate at least two slots.'
    )


# FUNCTIONS
# PAGES


class Demographics(Page):
    form_model = 'player'
    form_fields = [ 'age', 'gender', 'field_of_study',
                   'prior_experience', 'frequency_of_usage']

    def error_message(self, values):
        # Custom validation for age field
        age = values.get('age')
        if age is not None:
            if age < 18:
                return 'Please enter an age of at least 18.'
            elif age > 65:
                return 'Please enter an age of 65 or less.'

class End(Page):
    form_model = 'player'
    form_fields = [ ]

page_sequence = [ Demographics, End]
