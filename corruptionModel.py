import enum
import matplotlib.pyplot as plt
import pandas as pd

class CorruptionEnum(enum.Enum):
    CORRUPTION_LEVEL = "corruption level"
    GOVERNANCE_EFFECT = "goverance effect"
    ECONOMIC_DEVELOPMENT_EFFECT = "economic development"
    MEDIA_EXPOSURE_EFFECT = "media exposure"
    LAW_ENFORCEMENT_EFFECT = "law enforcement"

class Factor:
    def __init__(self, value, weight, update_delta, update_function):
        self.value = value
        self.weight = weight
        self.update_delta = update_delta
        self.update = update_function
        self.value_history = []


class CorruptionModel:
    def __init__(self, factors, iterations, initial_corruption, corruption_decay, calculate_corruption):
        self.factors = factors

        self.corruption = initial_corruption
        self.corruption_history = []
        self.corruption_decay = corruption_decay
        self.calculate_corruption = calculate_corruption


        self.iterations = iterations


    def observe(self, new_corruption):
        self.corruption = new_corruption
        self.corruption_history.append(new_corruption)

    def update_system(self):
        for factor_name, factor in self.factors.items():
            factor.value = factor.update(factor.value, factor.update_delta)
            factor.value_history.append(factor.value)

        return self.calculate_corruption(self.corruption, self.corruption_decay, self.factors)
    
    def model(self):
        corruption = self.corruption

        for time in range(self.iterations):
            self.observe(corruption)

            corruption = self.update_system()

    def get_corruption(self):
        return self.corruption

    def plot_phase_spaces(self, factor_name):
        if factor_name not in self.factors:
            return
        
        x_results = self.corruption_history
        y_results = self.factors[factor_name].value_history

        try:
            data = pd.DataFrame({'corruption': x_results, factor_name: y_results})
            fig, ax = plt.subplots()
            ax.scatter(x=x_results, y=y_results)
            plt.show()
        except Exception as e:
            print(e)