#⁠Filter the data to include only weekdays (Monday to Friday) and plot a line graph showing the pedestrian counts for each day of the week.

import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"

df = pd.read_csv(url)

# Convert 'hour_beginning' to datetime format
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

# Extract the day of the week
df['DayOfWeek'] = df['hour_beginning'].dt.day_name()

# Filter for weekdays only (Monday to Friday)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
df_weekdays = df[df['DayOfWeek'].isin(weekdays)]

# Group by day of the week and sum pedestrian counts
pedestrian_counts = df_weekdays.groupby('DayOfWeek')['Pedestrians'].sum()

# Reorder to match weekday order
pedestrian_counts = pedestrian_counts.reindex(weekdays)

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(pedestrian_counts.index, pedestrian_counts.values, marker='o', linestyle='-', color='b')
plt.xlabel("Day of the Week")
plt.ylabel("Total Pedestrian Count")
plt.title("Pedestrian Counts for Each Weekday on Brooklyn Bridge")
plt.grid(True)
plt.show()