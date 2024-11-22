from otree.api import*

doc = """PVQ"""


class C(BaseConstants):
    NAME_IN_URL = 'time'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIMESLOTS = ['date1',
                 'date2',
                 'date3']



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    date1= models.BooleanField(blank=True)
    date2 = models.BooleanField(blank=True)
    date3 = models.BooleanField(blank=True)


    interest_to_participate = models.BooleanField(
        label='I have understood the data that will be collected in Part B. I would like to participate in Part B of this experiment in KD2 Lab.',
        widget=widgets.CheckboxInput
    )


class Consent(Page):
    form_model = 'player'
    form_fields = ['interest_to_participate'] + C.TIMESLOTS  # Combine the static field with TIMESLOTS list

    def error_message(self, values):
        # Count the selected timeslots
        selected_timeslots = sum(1 for slot in C.TIMESLOTS if values[slot])

        # Check if 'interest_to_participate' is True and fewer than 2 timeslots are selected
        if values['interest_to_participate'] and selected_timeslots < 2:
            return 'Please select at least two timeslots to participate.'

page_sequence = [Consent]