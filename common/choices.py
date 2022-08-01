################# gender #######################33
FEMALE = 'female'
MALE = 'male'

GENDER = (
    (FEMALE, 'female'),
    (MALE, 'male')
)


############# currency ###########################
UZS = 'uzs'
USD = 'usd'

CURRENCY = (
    (UZS, 'uzs'),
    (USD, 'usd')
)

################ degree type #########################
SECONDARY_EDU = 'secondary edu'
SPECIALIZED_SECONDARY_EDU = 'specialized secondary edu'
UNFINISHED_HIGHER_EDU = 'unfinished higher edu'
BACHELORS = 'bachelors'
MASTERS = 'masters'
PHD = 'phd'
DC = 'dc'
INTERNSHIP = 'internship'

STUDY_DEGREE = (
    (SECONDARY_EDU, 'secondary edu'),
    (SPECIALIZED_SECONDARY_EDU, 'specialized secondary edu'),
    (UNFINISHED_HIGHER_EDU, 'unfinished higher edu'),
    (BACHELORS, 'bachelors'),
    (MASTERS, 'masters'),
    (PHD, 'phd'),
    (DC, 'dc'),
    (INTERNSHIP, 'internship')
)


############## language levels ##################
NATIVE = 'native'
C1 = 'c1'
C2 = 'c2'
B2 = 'b2'
B1 = 'b1'

LEVELS = (
    (NATIVE, 'native'),
    (C1, 'c1'),
    (C2, 'c2'),
    (B2, 'b2')
)


############## working mode ################
FULL_TIME = 'full time'
PART_TIME = 'part time'
INTERNSHIP = 'internship'
REMOTE = 'remote'


EMPLOYMENT_TYPE = (
    (FULL_TIME, 'full time'),
    (PART_TIME, 'part time'),
    (INTERNSHIP, 'internship'),
    (REMOTE, 'remote'),
)

