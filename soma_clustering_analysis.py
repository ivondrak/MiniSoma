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

# Plot clustered SOM map
plt.figure(figsize=(10, 8))
plt.pcolor(cluster_map, cmap='tab10', alpha=0.7)  # Color clusters
plt.colorbar(label="Cluster Label")

# Overlay best matching units (BMUs)
for i, x in enumerate(data_scaled):
    bmu = som.winner(x)
    plt.plot(bmu[0] + 0.5, bmu[1] + 0.5, 'ko', markersize=4)  # Mark BMUs

plt.title("Shluková analýza na 2D SOM mapě")
plt.show()