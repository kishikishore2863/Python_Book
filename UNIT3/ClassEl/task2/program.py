import pandas as pd

df = pd.read_csv('./../Movie Assignment Data for Class.csv')

df["budget"] = df['budget'].apply(lambda x:x+5000)
print(df)