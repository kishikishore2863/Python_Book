try:
    with open('t3.txt', 'w') as f:
        data = input("enter content")
        f.write(data)
except Exception:
    print(Exception)