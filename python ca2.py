import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('C:/Users/HP/Downloads/Crime_Incidents_in_2025.csv')

# Convert report date to datetime
df['REPORT_DAT'] = pd.to_datetime(df['REPORT_DAT'])

# Extract month and hour
df['Month'] = df['REPORT_DAT'].dt.to_period('M').dt.strftime('%Y-%m')
df['Hour'] = df['REPORT_DAT'].dt.hour

# Set style
sns.set(style='whitegrid')

# 1. Monthly crime trend
plt.figure(figsize=(12, 6))
monthly_counts = df['Month'].value_counts().sort_index()
sns.lineplot(x=monthly_counts.index, y=monthly_counts.values, marker='o')
plt.xticks(rotation=45)
plt.title('Monthly Crime Trend')
plt.xlabel('Month')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.show()

# 2. Top 10 crime types
plt.figure(figsize=(10, 6))
top_offenses = df['OFFENSE'].value_counts().head(10)
sns.barplot(y=top_offenses.index, x=top_offenses.values, hue=top_offenses.index, palette='mako', dodge=False, legend=False)
plt.title('Top 10 Crime Types')
plt.xlabel('Number of Crimes')
plt.ylabel('Crime Type')
plt.tight_layout()
plt.show()

# 3. Crimes by shift
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='SHIFT', hue='SHIFT', palette='coolwarm', legend=False, order=df['SHIFT'].value_counts().index)
plt.title('Crimes by Shift')
plt.xlabel('Shift')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.show()

# 4. Crimes by district
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='DISTRICT', hue='DISTRICT', palette='viridis', legend=False)
plt.title('Crimes by District')
plt.xlabel('District')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.show()

# 5. Heatmap: Offense vs. Shift
plt.figure(figsize=(12, 8))
heat_df = pd.crosstab(df['OFFENSE'], df['SHIFT'])
sns.heatmap(heat_df, cmap='YlOrBr', annot=True, fmt='d')
plt.title('Crime Types vs. Shifts Heatmap')
plt.tight_layout()
plt.show()


# 6. Crime frequency by hour of the day
plt.figure(figsize=(12, 6))
sns.countplot(x='Hour', data=df, palette='rocket')
plt.title('Crimes by Hour of Day')
plt.xlabel('Hour of Day (0–23)')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.show()


# 7. Crimes by Neighborhood Cluster (Top 10)
plt.figure(figsize=(12, 6))
top_clusters = df['NEIGHBORHOOD_CLUSTER'].value_counts().head(10)
sns.barplot(x=top_clusters.values, y=top_clusters.index, palette='cubehelix')
plt.title('Top 10 Neighborhood Clusters by Crime Count')
plt.xlabel('Number of Crimes')
plt.ylabel('Neighborhood Cluster')
plt.tight_layout()
plt.show()
