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

"""
1.Selecting a single column, which yields a Series, equivalent to df.A
"""
print("df['A']:")
print(df['A'])

"""
2.Selecting via [], which slices the rows.
"""
print('df[:3]')
print(df[:3])
print('df[\'20130102\':\'20130104\']')
print(df['20130102':'20130104'])

"""
3.For getting a cross section using a label
"""
print('df.loc[dates[0]:')
print(df.loc[dates[0]])

"""
4.Selecting on a multi-axis by label
"""
print('df.loc[:, [\'A\', \'B\']]')
print(df.loc[:, ['A', 'B']])

"""
5.Showing label slicing, both endpoints are included
"""
print("df.loc['20130102':'20130104', ['A', 'B']]")
print(df.loc['20130102': '20130104', ['A', 'B']])

"""
6.Reduction in the dimensions of the returned object
"""
print("df.loc['20130102', ['A', 'B']]")
print(df.loc['20130102', ['A', 'B']])

"""
7.For getting fast access to a scalar (equiv to the prior method)
"""
print("df.at[dates[0], 'A']")
print(df.at[dates[0], 'A'])

"""
8.Select via the position of the passed integers
"""
print('df.iloc[3]:')  # 按照行读取 从0到开始
print(df.iloc[3])

"""
By lists of integer position locations, similar to the numpy/python style
"""
print("df.iloc[[1,2,4], [0,2]] :")
print(df.iloc[[1, 2, 4], [0, 2]])

"""
9.For slicing columns explicitly
"""
print("df.iloc[:, 1:3] :")
print(df.iloc[:, 1:3])

"""
10.For getting a value explicitly
"""
print("df.iloc[1, 1] :")
print(df.iloc[1, 1])

"""
11.For getting fast access to a scalar (equiv to the prior method)
"""
print("df.iat[1, 1] :")
print(df.iat[1, 1])

"""
12.Boolean Index:
Using a single column's values to select data
"""
print("df[df.A > 0]")
print(df[df.A > 0])

"""
13.A where operation for getting
"""
print("df[df > 0] :")
print(df[df > 0])

"""
14.Using the isin() method for filtering:
"""
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print("df2:")
print(df2)
var_1 = df2[df2['E'].isin(['two', 'four'])]
print(var_1)


# --------------------------------------------------------------------------------

"""
Setting a new column automatically aligns the data by the indexes
"""
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print("s1:")
print(s1)

df['F'] = s1
print(df)

# Setting values by label
df.at[dates[0], 'A'] = 0
# Setting values by position
df.iat[0, 1] = 0
# Setting by assigning with a numpy array
df.loc[:, 'D'] = np.array([5] * len(df))
print("new df:")
print(df)

# A where operation setting.
df2 = df.copy()
df2[df2 > 0] = -df2
print("new df2:")
print(df2)

# --------------------------------------------------------------------------------

"""
Missing Data
"""
df1 = df.reindex(index=dates[0: 4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]: dates[1], 'E'] = 1
print("new df1:")
print(df1)

# To drop any rows that have missing data.
print("df1.dropna(how='any') : ")
print(df1.dropna(how='any'))

# Filling missing data
print("df1.fillna(value=5) ：")

print("after - fill :")
print(df1.fillna(value=5))

# To get the boolean mask where values are NaN
print("pd.isnull(df1):")
print(pd.isnull(df1))

# --------------------------------------------------------------------------------

"""
Stats
operation in general exclude missing data
Performing a descriptive statistic
"""
print("df.mean():")
print(df.mean())

# Same operation on the other axis
print("df.mean(1):")
print(df.mean(1))

# Operation with objects that have different dimensionality and need alignment. In addition,
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print("s:")
print(s)
print(df.sub(s, axis='index'))

# --------------------------------------------------------------------------------

"""
Applying functions to data
"""
print("apply-cumsum")
print(df.apply(np.cumsum))
temp = df.apply(lambda x: x.max() - x.min())
print("temp:", temp)

# --------------------------------------------------------------------------------

"""
Histogramming
"""
s = pd.Series(np.random.randint(0, 7, size=10))
print("s:", s)

# --------------------------------------------------------------------------------

"""
String Methods
Series is equipped with a set of string processing methods in the str attribute that make it easy to operate on each
element of the array, as in the code snippet below. Note that pattern-matching in str generally uses regular expressions
by default (and in some cases always uses them).
"""
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s)
print("s.str.lower():")
print(s.str.lower())

# --------------------------------------------------------------------------------

"""
Merge
Concat
pandas provides various facilities for easily combining together Series, DataFrame, and Panel objects with various
kinds of set logic for the indexes and relational algebra functionality in the case of join / merge-type operations.
"""
# Concatenating pandas objects together with concat():
df = pd.DataFrame(np.random.randn(10, 4))
print("concat-df:")
print(df)
# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
print("pd.concat(pieces) ：")
print(pd.concat(pieces))

# --------------------------------------------------------------------------------

"""
Join
"""
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print("left:", left)
print("right:", right)
temp = pd.merge(left, right, on='key')
print("merge:")
print(temp)
# Another example that can be given is:
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print("left:")
print(left)
print("right:")
print(right)
temp = pd.merge(left, right, on='key')
print("merge:")
print(temp)

# --------------------------------------------------------------------------------

"""
Append
"""
# Append rows to a dataframe. See the Appending
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print("df:", df)
s = df.iloc[3]
print("s:", s)
temp = df.append(s, ignore_index=True)
print("temp:", temp)

# --------------------------------------------------------------------------------

"""
Grouping
By “group by” we are referring to a process involving one or more of the following steps
• Splitting the data into groups based on some criteria
• Applying a function to each group independently
• Combining the results into a data structure
"""
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
 'foo', 'bar', 'foo', 'foo'],
 'B' : ['one', 'one', 'two', 'three',
 'two', 'two', 'one', 'three'],
 'C' : np.random.randn(8),
 'D' : np.random.randn(8)})
print(df)
# Grouping and then applying a function sum to the resulting groups.
temp = df.groupby('A').sum()
print("temp:")
print(temp)

# grouping by multiple columns forms a hierarchical index, which are then apply then function
temp = df.groupby(['A', 'B']).sum()
print('temp:')
print(temp)

# --------------------------------------------------------------------------------

"""
Stack
"""
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
print("df2:", df2)
stacked = df2.stack()
print("stacked:", stacked)












