from otree.api import *

doc = """PVQ"""


class C(BaseConstants):
    NAME_IN_URL = 'pvq'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5, 6], widget=widgets.RadioSelect)



class Player(BasePlayer):
    attention_check = models.IntegerField(initial=0)
    q1 = make_q('It is important to him/her to form his/her views independently.')
    q2 = make_q('It is important to him/her that his/her country is secure and stable.')
    q3 = make_q('It is important to him/her to have a good timeslots.')
    q4 = make_q('It is important to him/her to avoid upsetting other people.')
    q5 = make_q('It is important to him/her that the weak and vulnerable in society be protected.')
    q6 = make_q('It is important to him/her that people do what he/she says they should.')
    q7 = make_q('It is important to him/her never to think he/she deserves more than other people.')
    q8 = make_q('It is important to him/her to care for nature.')
    q9 = make_q('It is important to him/her that no one should ever shame him/her.')
    q10 = make_q('It is important to him/her always to look for different things to do.')
    q11 = make_q('It is important to him/her to take care of people he/she is close to.')
    q12 = make_q('It is important to him/her to have the power that money can bring.')
    q13 = make_q('It is very important to him/her to avoid disease and protect his/her health.')
    q14 = make_q('It is important to him/her to be tolerant toward all kinds of people and groups.')
    q15 = make_q('It is important to him/her never to violate rules or regulations.')
    q16 = make_q('It is important to him/her to make his/her own decisions about his/her life.')
    q17 = make_q('It is important to him/her to have ambitions in life.')
    q18 = make_q('It is important to him/her to maintain traditional values and ways of thinking.')
    q19 = make_q('It is important to him/her that people he/she knows have full confidence in him/her.')
    q20 = make_q('It is important to him/her to be wealthy.')
    q21 = make_q('It is important to him/her to take part in activities to defend nature.')
    q22 = make_q('It is important to him/her never to annoy anyone.')
    q23 = make_q('It is important to him/her to develop his/her own opinions.')
    q24 = make_q('It is important to him/her to protect his/her public image.')
    q25 = make_q('It is very important to him/her to help the people dear to him/her.')
    q26 = make_q('It is important to him/her to be personally safe and secure.')
    q27 = make_q('It is important to him/her to be a dependable and trustworthy friend.')
    q28 = make_q('It is important to him/her to take risks that make life exciting.')
    q29 = make_q('It is important to him/her to have the power to make people do what he/she wants.')
    q30 = make_q('It is important to him/her to plan his/her activities independently.')
    q31 = make_q('It is important to him/her to follow rules even when no one is watching.')
    q32 = make_q('It is important to him/her to be very successful.')
    q33 = make_q('It is important to him/her to follow his/her family’s customs or the customs of a religion.')
    q34 = make_q('It is important to him/her to listen to and understand people who are different from him/her.')
    q35 = make_q('It is important to him/her to have a strong state that can defend its citizens.')
    q36 = make_q('It is important to him/her to enjoy life’s pleasures.')
    q37 = make_q('It is important to him/her that every person in the world have equal opportunities in life.')
    q38 = make_q('It is important to him/her to be humble.')
    q39 = make_q('It is important to him/her to figure things out himself/herself.')
    q40 = make_q('It is important to him/her to honor the traditional practices of his/her culture.')
    q41 = make_q('It is important to him/her to be the one who tells others what to do.')
    q42 = make_q('It is important to him/her to obey all the laws.')
    q43 = make_q('It is important to him/her to have all sorts of new experiences.')
    q44 = make_q('It is important to him/her to own expensive things that show his/her wealth.')
    q45 = make_q('It is important to him/her to protect the natural environment from destruction or pollution.')
    q46 = make_q('It is important to him/her to take advantage of every opportunity to have fun.')
    q47 = make_q('It is important to him/her to concern himself/herself with every need of his/her dear ones.')
    q48 = make_q('It is important to him/her that people recognize what he/she achieves.')
    q49 = make_q('It is important to him/her never to be humiliated.')
    q50 = make_q('It is important to him/her that his/her country protect itself against all threats.')
    q51 = make_q('It is important to him/her never to make other people angry.')
    q52 = make_q('It is important to him/her that everyone be treated justly, even people he/she doesn’t know.')
    q53 = make_q('It is important to him/her to avoid anything dangerous.')
    q54 = make_q('It is important to him/her to be satisfied with what he/she has and not ask for more.')
    q55 = make_q('It is important to him/her that all his/her friends and family can rely on him/her completely.')
    q56 = make_q('It is important to him/her to be free to choose what he/she does by himself/herself.')
    q57 = make_q('It is important to him/her to accept people even when he/she disagrees with them.')
    attention1 = make_q('It is important to him/her to select the option "Not like me at all " to show that he/she is answering the questions attentively.')
    attention2 = make_q('It is important to him/her to select the option "Not like me " to show that he/she is answering the questions attentively.')
    attention3 = make_q('It is important to him/her to select the option "A little like me " to show that he/she is answering the questions attentively.')


    # Computed subscale scores
    unn = models.FloatField()  # Universalism-Nature: Preservation of the natural environment
    unc = models.FloatField()  # Universalism-Concern: Commitment to equality, justice, and protection for all people
    unt = models.FloatField()  # Universalism-Tolerance: Acceptance and understanding of those who are different from oneself
    bec = models.FloatField()  # Benevolence-Caring: Devotion to the welfare of in-group members
    bed = models.FloatField()  # Benevolence-Dependability: Being a reliable and trustworthy member of the in-group
    sdt = models.FloatField()  # Self-Direction-Thought: The freedom to cultivate one’s own ideas and abilities
    sda = models.FloatField()  # Self-Direction-Action: The freedom to determine one’s own actions
    he = models.FloatField()  # Hedonism: Definition unchanged
    ac = models.FloatField()  # Achievement: Definition unchanged
    pod = models.FloatField()  # Power-Dominance: Power through exercising control over people
    por = models.FloatField()  # Power-Resources: Power through control of material and social resources
    fac = models.FloatField()  # Face: Security and power through maintaining one’s public image and avoiding humiliation
    sep = models.FloatField()  # Security-Personal: Safety in one’s immediate environment
    ses = models.FloatField()  # Security-Societal: Safety and stability in the wider society
    tr = models.FloatField()  # Tradition: Maintaining and preserving cultural, family, or religious traditions
    cor = models.FloatField()  # Conformity-Rules: Compliance with rules, laws, and formal obligations
    coi = models.FloatField()  # Conformity-Interpersonal: Avoidance of upsetting or harming other people
    hum = models.FloatField()  # Humility: Recognizing one’s insignificance in the larger scheme of things
    st = models.FloatField()

def combine_score(value1, value2, value3):
    return value1 + value2 + value3


class SurveyPage1(Page):
        form_model = 'player'
        form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7','q8', 'q9', 'q10']

class SurveyPage2(Page):
        form_model = 'player'
        form_fields = ['q11', 'q12', 'q13', 'q14',  'attention1', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20']

        @staticmethod
        def before_next_page(player: Player, timeout_happened):
            if player.attention1 != 1:
                player.attention_check += 1


class SurveyPage3(Page):
        form_model = 'player'
        form_fields = ['q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30']

class SurveyPage4(Page):
        form_model = 'player'
        form_fields = ['q31', 'q32', 'q33', 'q34', 'attention2', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40']

        @staticmethod
        def before_next_page(player: Player, timeout_happened):
            if player.attention2 != 2:
                player.attention_check += 1
class SurveyPage5(Page):
        form_model = 'player'
        form_fields = ['q41', 'q42', 'q43', 'q44', 'q45', 'attention3', 'q46', 'q47', 'q48', 'q49', 'q50']

        @staticmethod
        def before_next_page(player: Player, timeout_happened):
            if player.attention3 != 3:
                player.attention_check += 1

class SurveyPage6(Page):
        form_model = 'player'
        form_fields = ['q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57']

        @staticmethod
        def before_next_page(player: Player, timeout_happened):
            player.unn = combine_score(player.q8, player.q21, player.q45)
            player.unc = combine_score(player.q5, player.q37, player.q52)
            player.unt = combine_score(player.q14, player.q34, player.q57)
            player.bec = combine_score(player.q11, player.q25, player.q47)
            player.bed = combine_score(player.q19, player.q27, player.q55)
            player.sdt = combine_score(player.q1, player.q23, player.q39)
            player.sda = combine_score(player.q16, player.q30, player.q56)
            player.he = combine_score(player.q3, player.q36, player.q46)
            player.ac = combine_score(player.q17, player.q32, player.q48)
            player.pod = combine_score(player.q6, player.q29, player.q41)
            player.por = combine_score(player.q12, player.q20, player.q44)
            player.fac = combine_score(player.q9, player.q24, player.q49)
            player.sep = combine_score(player.q13, player.q26, player.q53)
            player.ses = combine_score(player.q2, player.q35, player.q50)
            player.tr = combine_score(player.q18, player.q33, player.q40)
            player.cor = combine_score(player.q15, player.q31, player.q42)
            player.coi = combine_score(player.q4, player.q22, player.q51)
            player.hum = combine_score(player.q7, player.q38, player.q54)
            player.st = combine_score(player.q10, player.q28, player.q43)


class Results(Page):
    pass


page_sequence = [SurveyPage1, SurveyPage2, SurveyPage3, SurveyPage4, SurveyPage5, SurveyPage6]
