import matplotlib.pyplot as plt
import pandas as pd
from corruptionModel import CorruptionEnum, Factor, CorruptionModel
import enum

def update_factor(value, delta):
    return value + delta


def calculate_corruption(corruption, corruption_decay, factors):
    governance = factors[CorruptionEnum.GOVERNANCE_EFFECT]
    economic_development = factors[CorruptionEnum.ECONOMIC_DEVELOPMENT_EFFECT]
    media_exposure = factors[CorruptionEnum.MEDIA_EXPOSURE_EFFECT]
    law_enforcement = factors[CorruptionEnum.LAW_ENFORCEMENT_EFFECT]

    return corruption - \
        corruption_decay*corruption + \
        governance.weight*governance.value + \
        economic_development.weight*economic_development.value - \
        media_exposure.weight*media_exposure.value - \
        law_enforcement.weight*law_enforcement.value


if __name__ == '__main__':
    iterations = 10000
    initial_corruption = 0.3
    corruption_decay = 0.02

    factors = {
        CorruptionEnum.GOVERNANCE_EFFECT:Factor(value=0.6,weight=0.1, update_delta=0.005, update_function=update_factor),
        CorruptionEnum.ECONOMIC_DEVELOPMENT_EFFECT:Factor(value=0.5,weight= 0.05, update_delta=0.003, update_function=update_factor),
        CorruptionEnum.MEDIA_EXPOSURE_EFFECT:Factor(value=0.4,weight=0.03, update_delta=-0.001, update_function=update_factor),
        CorruptionEnum.LAW_ENFORCEMENT_EFFECT:Factor(value=0.7,weight= 0.08, update_delta=0.002, update_function=update_factor),
    }


    modelHandler = CorruptionModel(
        factors=factors,
        iterations=iterations,
        initial_corruption=initial_corruption,
        corruption_decay=corruption_decay,
        calculate_corruption=calculate_corruption)

    modelHandler.model()

    print(modelHandler.get_corruption())

# TODO review how to plot the phase space
""" 
data = pd.DataFrame({'x_results': x_results, 'y_results': y_results})


fig, ax = plt.subplots()


ax.scatter(x=x_results, y=y_results)


plt.show()
 """