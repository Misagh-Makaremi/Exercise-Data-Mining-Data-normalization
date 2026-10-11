data = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
print('#7-3-a:')

# Define the value to normalize
value_to_normalize = 35

# Min-max normalization function
def min_max_normalization(data, value):
  """
  Normalizes a value to a range between 0.0 and 1.0 based on the min and max of the data.

  Args:
      data: A list of numerical data points.
      value: The value to normalize.

  Returns:
      The normalized value.
  """
  min_value = min(data)
  max_value = max(data)
  return (value - min_value) / (max_value - min_value)

# Normalize the value
normalized_value = min_max_normalization(data, value_to_normalize)

# Print result
print("Normalized value of", value_to_normalize, ":", normalized_value)

print('#7-3-b:')
# Define the value to normalize and standard deviation
value_to_normalize = 35
std_dev = 12.94

# Z-score normalization function
def z_score_normalization(data, value, std_dev):
  """
  Normalizes a value using z-score normalization based on the data mean and standard deviation.

  Args:
      data: A list of numerical data points.
      value: The value to normalize.
      std_dev: The standard deviation of the data.

  Returns:
      The normalized value.
  """
  mean = sum(data) / len(data)
  return (value - mean) / std_dev

# Normalize the value
normalized_value = z_score_normalization(data, value_to_normalize, std_dev)

# Print result
print("Normalized value of", value_to_normalize, ":", normalized_value)

print('#7-3-c:')
import numpy as np

# Value to be normalized
value_to_normalize = 35

# Normalization by decimal scaling
power = np.ceil(np.log10(np.max(np.abs(data))))

decimal_scaled_value = value_to_normalize / 10**power

print(f"Decimal scaled value of {value_to_normalize}: {decimal_scaled_value}")

