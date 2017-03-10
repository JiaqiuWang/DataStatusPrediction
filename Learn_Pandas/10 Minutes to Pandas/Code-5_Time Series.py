import pandas as pd
import numpy as np

"""
Time Series
pandas has simple, powerful, and efficient functionality
for performing resampling operations during frequency conversion
 (e.g., converting secondly data into 5-minutely data).
This is extremely common in, but not limited to, financial
"""
rng = pd.date_range('20120101', periods=100, freq='S')
print("rng:", rng)
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print("ts:")
print(ts)
temp = ts.resample('5Min').sum()
print("temp:")
print(temp)

# Time zone representation
rng = pd.date_range('20120306 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print('ts:')
print(ts)
ts_utc = ts.tz_localize('UTC')
print("ts_utc")
print(ts_utc)

# Convert to another time zone
avar = ts_utc.tz_convert('US/Eastern')
print("convert:", avar)

# Converting between time span representations

rng = pd.date_range('20120101', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print("ts:", ts)
ps = ts.to_period()







