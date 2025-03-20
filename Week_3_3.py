import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Convert 'hour_beginning' to datetime format
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

# Define a function to categorize time of day
def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

# Apply the function to create a new column
df['TimeOfDay'] = df['hour_beginning'].dt.hour.apply(categorize_time_of_day)

# Group by TimeOfDay and sum pedestrian counts
time_of_day_pedestrian_counts = df.groupby('TimeOfDay')['Pedestrians'].sum().reset_index()

# Sort by custom time of day order
time_of_day_order = ["Morning", "Afternoon", "Evening", "Night"]
time_of_day_pedestrian_counts['TimeOfDay'] = pd.Categorical(
    time_of_day_pedestrian_counts['TimeOfDay'], categories=time_of_day_order, ordered=True
)
time_of_day_pedestrian_counts = time_of_day_pedestrian_counts.sort_values('TimeOfDay')

# Display sorted pedestrian activity patterns
print("Pedestrian Activity by Time of Day:\n", time_of_day_pedestrian_counts)

# Plot the pedestrian activity patterns
plt.figure(figsize=(8, 5))
sns.barplot(x="TimeOfDay", y="Pedestrians", data=time_of_day_pedestrian_counts, palette="Blues")
plt.xlabel("Time of Day")
plt.ylabel("Total Pedestrian Count")
plt.title("Pedestrian Activity Patterns Throughout the Day")
plt.show()
