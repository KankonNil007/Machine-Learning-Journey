import pandas as pd

# Read data from csv files into a dataframe

df1 = pd.read_csv("02-Pandas/01-Introduction/products-100.csv", encoding="utf-8")
# Encoding have to be either utf-8 or latin1

print(df1)

# Read data from excel files into a dataframe

df2 = pd.read_excel("02-Pandas/01-Introduction/file_example_XLSX_5000.xlsx")

print(df2)

# Read data from json files into a dataframe

df3 = pd.read_json("02-Pandas/01-Introduction/house-price.json")

print(df3)