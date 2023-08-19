import matplotlib.pyplot as plt
import pandas as pd

import enum

class CorruptionEnum(enum.Enum):
    CORRUPTION_LEVEL = "corruption level"
    GOVERNANCE_EFFECT = "goverance effect"
    ECONOMIC_DEVELOPMENT_EFFECT = "economic development"
    MEDIA_EXPOSURE_EFFECT = "media exposure"
    LAW_ENFORCEMENT_EFFECT = "law enforcement"


delta_goverance_effect = 0.005
delta_economic_development_effect = 0.003
delta_media_exposure_effect = -0.001
delta_law_enforcement_effect = 0.002


goverance_effect_weight = 0.1
economic_development_effect_weight = 0.05
media_exposure_effect_weight = 0.03
law_enforcement_effect_weight = 0.08
corruption_decay_weight = 0.02

def get_next_corruption(corruption, goverance, economic_development_effect, media_exposure_effect, law_enforcement_effect):
    next_corruption = corruption - \
        corruption_decay_weight*corruption + \
        goverance_effect_weight*goverance + \
        economic_development_effect_weight*economic_development_effect - \
        media_exposure_effect_weight*media_exposure_effect - \
        law_enforcement_effect_weight * law_enforcement_effect

    return next_corruption

def update_system(corruption_state):

    for variable, value in corruption_state.items():
        if variable == CorruptionEnum.CORRUPTION_LEVEL:
            continue

        update_function = update_function_by_corruption_variable[variable]

        updated_value = update_function(value)

        corruption_state[variable] = updated_value

    return get_next_corruption(
        corruption_state[CorruptionEnum.CORRUPTION_LEVEL],
        corruption_state[CorruptionEnum.GOVERNANCE_EFFECT],
        corruption_state[CorruptionEnum.ECONOMIC_DEVELOPMENT_EFFECT],
        corruption_state[CorruptionEnum.MEDIA_EXPOSURE_EFFECT],
        corruption_state[CorruptionEnum.MEDIA_EXPOSURE_EFFECT],
        corruption_state[CorruptionEnum.LAW_ENFORCEMENT_EFFECT])



def update_goverance_effect(goverance_effect):

    goverance_effect += delta_goverance_effect

    return goverance_effect


def update_system_economic_development(economic_development_effect):
    economic_development_effect += delta_economic_development_effect

    return economic_development_effect


def update_media_exposure_effect(media_exposure_effect):
    media_exposure_effect += delta_media_exposure_effect

    return media_exposure_effect


def update_law_enforcement_effect(law_enforcement_effect):
    law_enforcement_effect += delta_law_enforcement_effect

    return law_enforcement_effect


update_function_by_corruption_variable = {
    CorruptionEnum.GOVERNANCE_EFFECT: update_goverance_effect,
    CorruptionEnum.ECONOMIC_DEVELOPMENT_EFFECT: update_system_economic_development,
    CorruptionEnum.MEDIA_EXPOSURE_EFFECT: update_media_exposure_effect,
    CorruptionEnum.LAW_ENFORCEMENT_EFFECT: update_law_enforcement_effect,
}


def initial_conditions(state, coefficient, end_time):

    return state, coefficient, end_time, []


def observe(value):

    corruption_variables_state[CorruptionEnum.CORRUPTION_LEVEL] = value

    return CorruptionEnum


coeff = 0.5


iterations = 10000


corruption_variables_state = {
    CorruptionEnum.CORRUPTION_LEVEL: 0.3,
    CorruptionEnum.GOVERNANCE_EFFECT: 0.6,
    CorruptionEnum.ECONOMIC_DEVELOPMENT_EFFECT: 0.5,
    CorruptionEnum.MEDIA_EXPOSURE_EFFECT: 0.4,
    CorruptionEnum.LAW_ENFORCEMENT_EFFECT: 0.7,
}


corruption = corruption_variables_state[CorruptionEnum.CORRUPTION_LEVEL]


for time in range(1):

    observe(corruption)

    corruption = update_system(corruption_variables_state)


print(corruption)

# TODO review how to plot the phase space
""" 
data = pd.DataFrame({'x_results': x_results, 'y_results': y_results})


fig, ax = plt.subplots()


ax.scatter(x=x_results, y=y_results)


plt.show()
 """