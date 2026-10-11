print('#6-3-a:')
data = [200, 300, 400, 600, 1000]

# Define functions for min-max normalization
def min_max_normalization(data, min_d=0, max_d=1):
  """
  Normalizes data to a range between min_d and max_d.

  Args:
      data: A list of numerical data points.
      min_d: Minimum value for the normalized range (default: 0).
      max_d: Maximum value for the normalized range (default: 1).

  Returns:
      A list of normalized data points.
  """
  return [(x - min(data)) / (max(data) - min(data)) * (max_d - min_d) + min_d for x in data]

# Apply min-max normalization with min = 0 and max = 1
normalized_data = min_max_normalization(data, min_d=0, max_d=1)

# Print results
print("Original data:", data)
print("Normalized data:", normalized_data)


print('#6-3-b:')
# Z-score normalization
def z_score_normalization(data):
  """
  Normalizes data to have a mean of 0 and a standard deviation of 1.

  Args:
      data: A list of numerical data points.

  Returns:
      A list of normalized data points.
  """
  import numpy as np
  mean = np.mean(data)
  std = np.std(data)
  return [(x - mean) / std for x in data]

# Apply z-score normalization
normalized_data = z_score_normalization(data)

# Print results
print("Original data:", data)
print("Normalized data:", normalized_data)

print('#6-3-c:')
# Z-score normalization with MAD
def z_score_mad_normalization(data):
  """
  Normalizes data to have a median of 0 and a scaled median absolute deviation.

  Args:
      data: A list of numerical data points.

  Returns:
      A list of normalized data points.
  """
  import numpy as np

  median = np.median(data)
  mad = np.median(np.abs(data - median))
  return [(x - median) / (c * mad) for x in data]

# Choose scaling factor (commonly 1)
c = 1

# Apply z-score normalization with MAD
normalized_data = z_score_mad_normalization(data)

# Print results
print("Original data:", data)
print("Normalized data (z-score with MAD, c=", c, "):", normalized_data)

print('#6-3-d:')
import numpy as np

# Given data
data = np.array([200, 300, 400, 600, 1000])

# Normalization by decimal scaling
power = np.ceil(np.log10(np.max(np.abs(data))))

decimal_scaled_data = data / 10**power

print("Original data:", data)
print("Decimal scaled data:", decimal_scaled_data)
