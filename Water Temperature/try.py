import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create Antecedents and Consequent variables
waterPh = ctrl.Antecedent(np.arange(0, 15, 1), 'pH level of Water')

# # Define fuzzy sets for pH
waterPh['acidic'] = fuzz.trapmf(waterPh.universe, [0, 0, 4, 7])
waterPh['neutral'] = fuzz.trimf(waterPh.universe, [5, 7, 9])
waterPh['alkaline'] = fuzz.trapmf(waterPh.universe, [7, 10, 14, 15])

waterPh['neutral'].view()

plt.show()

# # Define fuzzy sets for fan_speed
# fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
# fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 50, 100])
# fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# # Define rules
# rule1 = ctrl.Rule(temperature['low'], fan_speed['low'])
# rule2 = ctrl.Rule(temperature['medium'], fan_speed['medium'])
# rule3 = ctrl.Rule(temperature['high'], fan_speed['high'])

# # Create Control System
# fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# # Create Simulation
# fan_simulation = ctrl.ControlSystemSimulation(fan_ctrl)

# # Pass input to the simulation
# fan_simulation.input['temperature'] = 20
# # Compute the output
# fan_simulation.compute()

# # Print the output
# print(fan_simulation.output['fan_speed'])

# # Plot the results
# temperature.view()
# fan_speed.view()
