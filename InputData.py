POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1/52       # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03
ADD_BACKGROUND_MORT = True

# transition matrix
#TRANS_MATRIX = [
#    [0.75,  0.15,   0.0,    0.1],   # Well
#    [0,     0.0,    1.0,    0.0],   # Stroke
#    [0,     0.25,   0.55,   0.2],   # Post-Stroke
#    [0.0,   0.0,    0.0,    1.0],   # Dead
#    ]

NO_Rate_Matrix = [# NO TREATMENT
[0,     0.0136,    0,   0.00151], # Well
[0,     0,         52,  0.00745], # Stroke
[0,     0.0298,    0,   0.00745], # Post-Stroke
[0,     0,         0,   0      ], # Stroke Death
]

AC_Rate_Matrix = [# ANTICOAGULANT
[0,     0.0136,    0,   0.00159], # Well
[0,     0,         52,  0.00745], # Stroke
[0,     0.0223,    0,   0.00782], # Post-Stroke
[0,     0,         0,   0      ], # Stroke Death
]

# anticoagulation relative risk in reducing stroke incidence and stroke death while in “Post-Stroke”
RR_STROKE = 0.65
# anticoagulation relative risk in increasing mortality due to bleeding is 1.05.
RR_BLEEDING = 1.05

ANNUAL_STATE_COST = [
    1,  # well
    0.2,  # stroke
    0.9,  # post-stroke
    0  # dead
]

ANNUAL_STATE_UTILITY = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0

]
TREAT_HEALTH_COST = [
    0,
    5000,  # stroke
    750,  # post-stroke /year
    0

]




Anticoag_COST = 2000

ANNUAL_PROB_BACKGROUND_MORT = 0.0176
