import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from minisom import MiniSom

# Load the dataset
file_path = "survey-data-technotrasa-numeric.xlsx"  # Change to your file path
xls = pd.ExcelFile(file_path)
df = xls.parse(xls.sheet_names[0])

# Convert all columns to numeric, forcing errors to NaN
df_numeric = df.apply(pd.to_numeric, errors='coerce')

# Check if df_numeric is empty
if df_numeric.empty:
    print("No numeric data found in the dataset.")
else:
    # Standardize the data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(df_numeric)

    # Check the standardized data
    print("Standardized data:")
    print(data_scaled)

    # Define SOM grid size
    som_size = (5, 5)

    # Initialize SOM
    som = MiniSom(som_size[0], som_size[1], data_scaled.shape[1], sigma=1.0, learning_rate=0.5)
    som.random_weights_init(data_scaled)

    # Train SOM with more iterations
    som.train_random(data_scaled, 1000)

    # Create a 2D visualization of SOM
    plt.figure(figsize=(10, 8))
    plt.pcolor(som.distance_map().T, cmap='coolwarm')  # U-matrix representation
    plt.colorbar(label="Neuronal distance")

    # Count the number of records in each cell
    win_map = som.win_map(data_scaled)
    for position, records in win_map.items():
        plt.text(position[0] + 0.5, position[1] + 0.5, str(len(records)),
                 color='black', ha='center', va='center', fontsize=12)

    plt.title("2D SOMA vizualizace pomocí MiniSom")
    plt.show()