import pandas as pd
import numpy as np


#creating a DataFrame from a list

s ="why common sense is not so common"
lst = s.split(" ")
df = pd.DataFrame(lst,columns=['words'])
print(df)


#creating a DataFrame from a dict
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(data,columns=['A','B','C'])
print(df)


import pandas as pd
dict ={'name':['kishore','kishi','kane','jhon'],
       'degree':['bsc','mtech','btech','mba']}

df = pd.DataFrame(dict)
print(df)
