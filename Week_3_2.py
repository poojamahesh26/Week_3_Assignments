import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Convert 'hour_beginning' to datetime format
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

# Filter data for the year 2019
df_2019 = df[df['hour_beginning'].dt.year == 2019]

# Group by weather summary and sum pedestrian counts
weather_pedestrian_counts = df_2019.groupby('weather_summary')['Pedestrians'].sum().reset_index()

# Sort the data by pedestrian counts in descending order
weather_pedestrian_counts = weather_pedestrian_counts.sort_values(by='Pedestrians', ascending=False)

# Display sorted pedestrian counts by weather summary
print("Weather Summary vs Pedestrian Counts (2019):\n", weather_pedestrian_counts)

# Select relevant numerical columns for correlation analysis
corr_columns = ['Pedestrians', 'temperature', 'precipitation']
df_corr = df_2019[corr_columns].dropna()  # Drop NaN values

# Compute correlation matrix
corr_matrix = df_corr.corr()

# Plot the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix: Weather Factors vs Pedestrian Counts (2019)")
plt.show()
