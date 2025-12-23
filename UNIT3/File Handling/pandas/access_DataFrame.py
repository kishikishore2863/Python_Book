import pandas as pd

data = {'name':['kishi','kishore','knae','jhon'],
        'age':[11,12,13,14],
        'gender':['male','male','female','male']
        }

df = pd.DataFrame(data)
print(df)

df = df.set_index('name')

age_column = df['age']
print(age_column)

