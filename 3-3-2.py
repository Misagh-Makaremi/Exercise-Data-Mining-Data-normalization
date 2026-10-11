# Sample data
data = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

# Define bin depth
bin_depth = 3

# Step 1: Find the number of bins
num_bins = len(data) // bin_depth

# Step 2: Create bins and assign data points to each bin
bins = []
for i in range(num_bins):
    start_index = i * bin_depth
    end_index = min((i + 1) * bin_depth, len(data))
    bin_data = data[start_index:end_index]
    bins.append(bin_data)

# Step 3: Calculate the mean of each bin
smoothed_data = []
for bin_ in bins:
    smoothed_data.append(sum(bin_) / len(bin_))

# Print original and smoothed data
print("Original data:", data)
print("Smoothed data:", smoothed_data)

# Effect of smoothing on the data
print("\nEffect of smoothing:")

# Original data has variations within similar age ranges (e.g., multiple values at 16, 20, 25, 35).
# Smoothed data replaces these variations with the average value of the bin, reducing the fluctuations.

# This technique can be helpful for:
# - Reducing noise in the data
# - Highlighting general trends rather than specific details
# - Simplifying the data for visualization

# However, it can also lead to:
# - Loss of information about individual data points
# - Masking potential outliers within a bin


# 2. Z-scores
def find_outliers_zscore(data):
  """
  Identifies outliers using Z-score method (threshold = 3).

  Args:
      data: A list of numerical data points.

  Returns:
      A list of potential outliers.
  """
  import numpy as np
  mean = np.mean(data)
  std = np.std(data)
  z_scores = [(x - mean) / std for x in data]
  outliers = [data[i] for i, score in enumerate(z_scores) if abs(score) > 3]
  return outliers

outliers_zscore = find_outliers_zscore(data)
print("\nOutliers (Z-score method, threshold=3):", outliers_zscore)


# 1. Interquartile Range (IQR)
def find_outliers_iqr(data):
  """
  Identifies outliers using Interquartile Range (IQR) method.

  Args:
      data: A list of numerical data points.

  Returns:
      A list of potential outliers.
  """
  q1 = sorted(data)[len(data) // 4]  # Calculate first quartile
  q3 = sorted(data)[3 * len(data) // 4]  # Calculate third quartile
  iqr = q3 - q1
  upper_bound = q3 + 1.5 * iqr
  lower_bound = q1 - 1.5 * iqr
  outliers = [x for x in data if x < lower_bound or x > upper_bound]
  return outliers

outliers_iqr = find_outliers_iqr(data)
print("\nOutliers (IQR method):", outliers_iqr)
