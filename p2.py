import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Load the data with the correct path format
data = pd.read_csv("D:\\Python\\ACS\\port.csv")

# Plot the data
plt.figure(figsize=(10,6))
sns.histplot(data['Total Tonnage (Million Tons)'], kde=True, bins=15)
plt.title('Distribution of Total Tonnage in Million Tons by Port')
plt.xlabel('Total Tonnage (Million Tons)')
plt.ylabel('Frequency')
plt.show()

# Calculate skewness and kurtosis
skewness = skew(data['Total Tonnage (Million Tons)'])
kurt = kurtosis(data['Total Tonnage (Million Tons)'])

# Print the skewness and kurtosis
print("Skewness:", skewness)
print("Kurtosis:", kurt)
