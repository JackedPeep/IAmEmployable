import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import wfdb
import numpy as np
from scipy import stats

# Use 'rdsamp' to read the .dat file
signals, fields = wfdb.rdsamp('data/1001')

# Assuming that you want to analyze the first column
data = signals[:, 1]

# Replace zeros with NaN
data[data == 0] = np.nan

# Calculate z-scores for non-zero (non-NaN) values
z_scores = stats.zscore(data[~np.isnan(data)])

# Identify outliers among the non-zero values
outliers = np.abs(z_scores) > 3

# Get original indices of the non-zero values
non_zero_indices = np.where(~np.isnan(data))

# Map the outliers identified in the non-zero values back to the original data
outlier_indices = non_zero_indices[0][outliers]

# Replace outliers with NaN in the original data
data[outlier_indices] = np.nan

# Define the ARIMA model
model = ARIMA(data, order=(2,0,1))

num_nan = np.isnan(data).sum()

# Fit the model
model_fit = model.fit()

# Make predictions
num_predictions = num_nan
predictions = model_fit.predict(start=len(data), end=len(data)+num_predictions-1, dynamic=False)

# Identify indices of missing values
missing_indices = np.where(np.isnan(data))

# Replace missing values with predictions
data[missing_indices] = predictions[:len(missing_indices[0])]



print('Number of NaN values:', num_nan)

print('Predicted Values:', predictions)

plt.plot(data)
plt.show()

