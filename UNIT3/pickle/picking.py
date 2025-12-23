import pickle

my_list = ['apple', 'banana','cherrry']
with open('list.pkl', 'wb')as file:
    pickle.dump(my_list,file)
with open('list.pkl', 'rb')as file:
    loaded_list = pickle.load(file)
print("Loaded list:",loaded_list)
