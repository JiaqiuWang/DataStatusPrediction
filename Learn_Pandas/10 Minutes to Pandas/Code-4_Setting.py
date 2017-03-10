import pandas as pd
import numpy as np

"""
Creating a Series by passing a list of values,
 letting pandas create a default integer index:
"""
s = pd.Series([1, 3, np.nan, 6, 8])
# print("s:", s)


"""
Creating a DataFrame by passing a numpy array,
with a datetime index and labeled columns:
"""
dates = pd.date_range('20130101', periods=6)
# print('dates:')
# print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("df:")
print(df)

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print("s1:")
print(s1)





