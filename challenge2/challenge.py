#Challenge laboratory 2 David Alejandro Melendez, Juan Camilo Ramirez, Juan Daniel Casanova, Nicolas David Rogers
import pandas as pd

def simulate_equation(x_cte, A, C, num_steps):
    results = [x_cte]

    for _ in range(num_steps):
        x_cte = x_cte - A * C * x_cte
        results.append(x_cte)

    return results

# Initial Conditions
x_cte_initial = [0, 2]
y_cte_initial = [0, 1]
A = 0.1
C_1 = 0.01
C_2 =  0.2
n_steps = 1000

sim_df1 = []
sim_df2 = []
for i in x_cte_initial:
    simulate_data1 = simulate_equation(22, A, C_1, n_steps)
    in_cond = [i] * len(simulate_data1)
    in_cond_data = {f'Initial condition {i}': in_cond,
                    f'Data_(1)': simulate_data1}
    in_cond_data = pd.DataFrame(in_cond_data)
    sim_df1.append(in_cond_data)

for i in y_cte_initial:
    simulate_data2 = simulate_equation(22, A, C_2, n_steps)
    in_cond1 = [i] * len(simulate_data2)
    in_cond_data1 = {f'Initial condition {i}': in_cond1,
                    f'Data_(1)': simulate_data2}
    in_cond_data1 = pd.DataFrame(in_cond_data1)
    sim_df2.append(in_cond_data1)

print("X const initial")
print(sim_df1)

print("Y const initial")
print(sim_df2)
