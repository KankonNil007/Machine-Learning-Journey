import pandas as pd

data = {
    "Name": ["Sarah", "Michael", "Emma", "Robert", "Sophia", "James", "Olivia", "Daniel", "Isabella", "William"],
    "Age": [29, 42, 31, 58, 25, 47, 36, 51, 28, 44],
    "Salary": [31000, 48000, 39000, 52000, 28000, 44000, 41000, 59000, 33000, 46000],
    "Performance": [7.2, 6.5, 8.1, 5.9, 9.0, 6.3, 7.5, 6.9, 8.4, 7.1]
}

df = pd.DataFrame(data)

# Accessing a Single Column
print(df["Age"])

# Accessing Multiple Columns
print(df[["Name", "Age"]])

# Filtering Data using Condition
print(df[df["Performance"] > 7])

# Filtering Data using multiple conditions - & |
print(df[(df["Age"] > 40) & (df["Performance"] > 7)])