import pandas as pd

df = pd.read_csv('coalpublic2013.csv')

# FIX column name issue
df.columns = df.columns.str.strip()

# Now this will work
print(df[['Operating Company', 'Coal Supply Region']].describe())