import enum

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


class CorruptionModel:
    def __init__(self, factors, iterations, initial_corruption, corruption_decay, calculate_corruption):
        self.factors = factors

        self.corruption = initial_corruption
        self.corruption_decay = corruption_decay
        self.calculate_corruption = calculate_corruption

        self.iterations = iterations


    def observe(self, new_corruption):
        self.corruption = new_corruption

    def update_system(self):
        for factor_name, factor in self.factors.items():
            factor.value = factor.update(factor.value, factor.update_delta)

        return self.calculate_corruption(self.corruption, self.corruption_decay, self.factors)
    
    def model(self):
        corruption = self.corruption
        for time in range(self.iterations):
            self.observe(corruption)

            corruption = self.update_system()

    def get_corruption(self):
        return self.corruption