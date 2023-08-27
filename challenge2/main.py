import matplotlib.pyplot as plt
import pandas as pd


def intial_conditions(state, coefficient_1, coefficient_2, end_time):
    return state, coefficient_1, coefficient_2, end_time, []


def observe(result, state):
    return result.append(state)


def update_system(x_state, y_state, a, b, c):
    new_x_state = x_state - a * b * x_state
    new_y_state = y_state - a * c * y_state

    return new_x_state, new_y_state

def plot(x_results, y_results, x_label, y_label):
  fig, ax = plt.subplots()
  ax.scatter(x = x_results, y = y_results)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()

# Probar con 0.1 es el mejor caso y con 0.001 es el peor caso
a = 0.1
b = 0.01
c = 0.2
#iterations = 60*24
iterations = 400
x_stateVar, a, b, Time, x_results = intial_conditions(22, a, b, iterations)
y_stateVar, c, d, Time, y_results = intial_conditions(22, a, c, iterations)

for time in range(Time):
    observe(x_results, x_stateVar)
    observe(y_results, y_stateVar)
    x_stateVar, y_stateVar = update_system(x_stateVar, y_stateVar, a, b, c)
    if(time == 165):
      print("temp: ", y_results[time])
print("Temp medical room: ", x_results)
print(x_results[-1])
print("Temp organ bank: ", y_results)
print(y_results[-1])

data = pd.DataFrame({'x_results': x_results, 'y_results': y_results})

time_vs_medical_temp = pd.DataFrame({'time': [time for time in range(Time)], 'temperature': x_results})
time_vs_organ_temp = pd.DataFrame({'time': [time for time in range(Time)], 'temperature': y_results})

time = [time for time in range(Time)]
plot(time, x_results, "Time", "Temp medical room")
plot(time, y_results, "Time", "Temp organ bank")
#plot(x_results, y_results, "Temp medical room", "Temp organ bank")
