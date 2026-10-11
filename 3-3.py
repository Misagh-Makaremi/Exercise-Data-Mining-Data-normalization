data = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
import numpy as np

print('#3-3-a:')

# Bin depth
bin_depth = 3

# Calculate the number of bins
num_bins = len(data) // bin_depth

# Calculate bin means
bin_means = [np.mean(data[i * bin_depth : (i + 1) * bin_depth]) for i in range(num_bins)]

# Extend the last bin if there are remaining elements
if len(data) % bin_depth != 0:
    last_bin_mean = np.mean(data[num_bins * bin_depth:])
    bin_means.append(last_bin_mean)

# Create the smoothed data
smoothed_data = [bin_means[i // bin_depth] for i in range(len(data))]

# Print original and smoothed data
print("Original data:", data)
print("Smoothed data:", smoothed_data)


print('#3-3-b&c:')
#Z-scores
def find_outliers_zscore(data):
  import numpy as np
  mean = np.mean(data)
  std = np.std(data)
  z_scores = [(x - mean) / std for x in data]
  outliers = [data[i] for i, score in enumerate(z_scores) if abs(score) > 3]
  return outliers

outliers_zscore = find_outliers_zscore(data)
print("\nOutliers (Z-score method, threshold=3):", outliers_zscore)


#Interquartile Range (IQR)
def find_outliers_iqr(data):
  q1 = sorted(data)[len(data) // 4]  # Calculate first quartile
  q3 = sorted(data)[3 * len(data) // 4]  # Calculate third quartile
  iqr = q3 - q1
  upper_bound = q3 + 1.5 * iqr
  lower_bound = q1 - 1.5 * iqr
  outliers = [x for x in data if x < lower_bound or x > upper_bound]
  return outliers

outliers_iqr = find_outliers_iqr(data)
print("\nOutliers (IQR method):", outliers_iqr)


#Boxplot
import matplotlib.pyplot as plt

plt.figure()
plt.boxplot(data, notch=True)
plt.title("Boxplot of data")
plt.xlabel("Age")
plt.ylabel("Value")
plt.show()