try:
    with open('te.txt','w+')as f:
        print(f.readline())
except Exception as e :
    print(e)