import pandas as pd

df = pd.read_csv('products-100.csv')

# print the first 5 rows
print(df.head())

# print the last 5 rows
print(df.tail())

# print the information of the dataframe
print(df.info())

# print the description of the dataframe
print(df.describe())

# print the columns of the dataframe
print(df.columns)

# print the index of the dataframe
print(df.index)

# print the shape of the dataframe
print(df.shape)

# print the size of the dataframe
print(df.size)

# print the data types of the dataframe
print(df.dtypes)

# print the values of the dataframe
print(df.values)