import numpy as np
import pandas as pd

# Constants
R = 8.314  # J/(mol*K), gas constant

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(temp_celsius):
    return temp_celsius + 273.15

# Ranges for Ea, T1, and T2
Ea_values = np.arange(20000, 121000, 10000)  # Ea in J/mol (converted from kJ/mol)
T1_range = np.arange(celsius_to_kelvin(15), celsius_to_kelvin(41))  # T1 in Kelvin
T2_range = np.arange(celsius_to_kelvin(18), celsius_to_kelvin(41))  # T2 in Kelvin

# Prepare for storing results
results = []

# Iterate through Ea, T1, and T2 values
for Ea in Ea_values:
    for T1 in T1_range:
        for T2 in T2_range:
            if 3 <= (T2 - T1) <= 10:  # Ensuring the temperature difference is within the specified range
                ln_ratio = (Ea / R) * (1/T1 - 1/T2)
                D_ratio = np.exp(ln_ratio)  # D2/D1
                percent_increase = (D_ratio - 1) * 100  # Percentage increase of D2 over D1

                # Store the results
                results.append([Ea/1000, T1-273.15, T2-273.15, D_ratio, percent_increase])

# Convert results to a DataFrame
df_results = pd.DataFrame(results, columns=['Ea (kJ/mol)', 'T1 (°C)', 'T2 (°C)', 'D2/D1', 'Percent Increase'])

# Save the results to a CSV file
file_path = 'arrhenius_equation_results.csv'
df_results.to_csv(file_path, index=False)

print(f"Results saved to {file_path}")

