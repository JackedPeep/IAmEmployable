from statsmodels.tsa.arima.model import ARIMA
import wfdb
import numpy as np
from scipy import stats
import itertools
import warnings


# Use 'rdsamp' to read the .dat file
signals, fields = wfdb.rdsamp('data/1001')

# Assuming that you want to analyze the first column
data = signals[:, 0]

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

# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 3)

# Generate all different combinations of p, d and q triplets
pdq = list(itertools.product(p, d, q))

# Specify to ignore warning messages
warnings.filterwarnings("ignore")

best_aic = np.inf
best_pdq = None
temp_model = None

for param in pdq:
    try:
        temp_model = ARIMA(data,order=param)
        results = temp_model.fit()
        if results.aic < best_aic:
            best_aic = results.aic
            best_pdq = param
    except:
        continue

print("Best ARIMA model: ", best_pdq)
print("Best AIC: ", best_aic)