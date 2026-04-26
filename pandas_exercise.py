import pandas as pd
import numpy as np

# Dataset: Employee records with some missing values
data = {
    "name":       ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "department": ["ML", "Data", "ML", "Data", "ML", "Data"],
    "experience": [3, 5, None, 8, 2, 6],
    "salary":     [70000, 80000, 90000, None, 60000, 85000],
    "rating":     [4.5, 3.8, 4.2, 4.9, None, 3.5]
}

df = pd.DataFrame(data)

# Task 1: Print shape, info, and describe — what do you observe?
print(df.shape)
print(df.info()) # this shows that it indeed a dataframe and it has 6 enteries with 0 to 5, it shows it has total 5 columns and non-null 
#count is shared with the data types of each column. Also memory usage is shared
print(df.describe())

#observation - this is a 6 row by 5 column data,with 3 of those missing one value or having null value. as other two has 6 non-null
#data

# Task 2: Print only the ML department employees
print(df[df['department'] == 'ML'])
#one question, what if i need only name of employees here with ML department


# Task 3: Print name and salary columns only for employees 
#         with experience > 4 years
#         Note: missing experience values should NOT appear

print(df.loc[df["experience"]>4,["name","salary"]])

# Task 4: How many missing values are in each column?
# 1 missing value in 3 of the columns as given in pd.describe function as well as below method shows count of missing value per col
#print(df.isnull().sum())

# Task 5: Fill missing experience with the column mean
#         Fill missing salary with the column median
#         Fill missing rating with the column mean
#         Print the cleaned dataframe
df["experience"]=df["experience"].fillna(df["experience"].mean(numeric_only=True))
df["salary"]     = df["salary"].fillna(df["salary"].median())
df["rating"]     = df["rating"].fillna(df["rating"].mean())
print(df)


# Task 6: Add a new column "seniority" with values:
#         "junior" if experience < 4
#         "senior" if experience >= 4
#         Hint: look up pd.cut() or np.where()

import numpy as np

#df["seniority"] = np.where(df["experience"]<4,"junior","senior")
#print(df)
df["seniority_cuts"] = pd.cut(
                            df["experience"],
                             bins=[0,4,10],
                             labels=["junior","senior"])
print(df)