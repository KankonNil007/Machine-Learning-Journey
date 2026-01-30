import pandas as pd

data = {
    "Name": ["Darren", "John", "David"],
    "Age": [35, 34, 23],
    "City": ["Los Angeles", "Chicago", "Texas"]    
}

df = pd.DataFrame(data)

print(df)

# Data to CSV Saving
df.to_csv("02-Pandas/02-Data-Saving/output.csv", index=False)

# Data to Excel Saving
df.to_excel("02-Pandas/02-Data-Saving/output.xlsx", index=False)

# Data to JSON Saving
df.to_json("02-Pandas/02-Data-Saving/output.json", index=False)