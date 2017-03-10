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
# print("df:")
# print(df)

"""
1.See the top & bottom rows of the frame
"""
print("df.head():")
print(df.head())

"""
2.Display the index, columns, and the underlying numpy data
"""
print("df.index:")
print(df.index)
print("df.columns:")
print(df.columns)
print("df.value:")
print(df.values)

"""
3.Describe shows a quick statistic summary of your data
"""
print(df.describe())

"""
4.Transposing your data
"""
print("Transpose:")
print(df.T)

"""
5.Sorting by an axis
"""
print("Sorting by an axis:")
print(df.sort_index(axis=1, ascending=False))

"""
6.Sorting by values:
"""
print("Sorting by values:")
print(df.sort_values(by='B'))













