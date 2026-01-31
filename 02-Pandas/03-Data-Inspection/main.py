import pandas as pd

df = pd.read_csv("02-Pandas/01-Introduction/products-100.csv", encoding="utf-8")

# head(n) - prints first n rows
# Their default value is 5 if you don't pass a number

print("Display First 5 rows")
print(df.head(5))

# tail(n) - prints last n rows

print("Display Last 5 rows")
print(df.tail(5))


# info() method - summarize the dataset
# number of rows and columns
# column names
# data types
# non null counts
# memory usage

print("Displaying the info of the DataSet")
print(df.info())


# describe() method - summary for numerical columns

print("Descriptive Statistics")
print(df.describe())

data = {
    "Name": ["David","Smith","John","Alex","Marsh","Jason"],
    "Age": [34,54,23,53,65,64],
    "Salary": [23000,45000,34000,56000,35000,60000],
    "Performance": [4.5,5.6,7.8,6.7,8.8,6.8]
}

df2 = pd.DataFrame(data)

# .shape - displays the shape of the dataset

print(f"Shape: {df2.shape}")

# .columns - displays the column names

print(f"Column Names: {df2.columns}")

# .dtypes - displays the data types

print(f"Data Types: {df2.dtypes}")

# .sample(n) - shows random n rows

print(df2.sample())