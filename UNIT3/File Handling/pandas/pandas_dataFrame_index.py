import pandas as pd
data = {'name':['kishi','kishore','knae','jhon'],
        'age':[11,12,13,14],
        'gender':['male','male','female','male']
        }

df = pd.DataFrame(data)
print(df.index)

df = df.set_index('name')
print(df)
row = df.loc['kishi']
print(row)
