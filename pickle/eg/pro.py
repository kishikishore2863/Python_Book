import pandas as pd


data ={
    "name":["kishi","kishore","kane"],
    "age":[25,30,35],
    "city":['newyork',"blr","usa"]
}

df = pd.DataFrame(data)
df.to_pickle('dataframe.pkl')

loaded_pick = pd.read_pickle('dataframe.pkl')
print(loaded_pick)