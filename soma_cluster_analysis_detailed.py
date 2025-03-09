import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from minisom import MiniSom
from sklearn.cluster import KMeans

# Load the dataset
file_path = "survey-data-technotrasa-numeric.xlsx"  # Change this to your file path
xls = pd.ExcelFile(file_path)
df = xls.parse(xls.sheet_names[0])

# Select numerical columns
df_numeric = df.select_dtypes(include=['number']).dropna()

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df_numeric)

# Define SOM grid size
som_size = (5, 5)

# Initialize SOM
som = MiniSom(som_size[0], som_size[1], data_scaled.shape[1], sigma=1.0, learning_rate=0.5)
som.random_weights_init(data_scaled)

# Train SOM
som.train_random(data_scaled, 100)

# Apply KMeans clustering to the SOM weight vectors
num_clusters = 4  # Adjust if needed
som_weights = som.get_weights().reshape(-1, data_scaled.shape[1])  # Flatten SOM grid
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
labels = kmeans.fit_predict(som_weights)

# Reshape labels back to SOM grid
cluster_map = labels.reshape(som_size[0], som_size[1])

# Assign clusters to respondents
bmu_indexes = np.array([som.winner(x) for x in data_scaled])  # Get BMU for each respondent
bmu_labels = np.array([cluster_map[bmu[0], bmu[1]] for bmu in bmu_indexes])  # Assign cluster labels

df_numeric["Cluster"] = bmu_labels

# 1️⃣ **Porovnání průměrných charakteristik v každém shluku**
cluster_means = df_numeric.groupby("Cluster").mean()
print("Průměrné hodnoty v jednotlivých shlucích:\n", cluster_means)

# 2️⃣ **Zjistíme, které odpovědi jsou pro každý shluk typické**
cluster_modes = df_numeric.groupby("Cluster").agg(lambda x: x.value_counts().idxmax())
print("Typické odpovědi v jednotlivých shlucích:\n", cluster_modes)

# 3️⃣ **Vykreslení grafu s počtem respondentů v každém shluku**
plt.figure(figsize=(8, 6))
df_numeric["Cluster"].value_counts().sort_index().plot(kind="bar", color="royalblue", alpha=0.7)
plt.xlabel("Shluk")
plt.ylabel("Počet respondentů")
plt.title("Rozložení respondentů podle shluku")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
