try:
    with open('t2.txt','r') as f:
        lines = f.readlines()
        if not lines:
            raise ValueError("file is empty")

        for i in range(min(5,len(lines))):
            print(lines[i].strip())

except ValueError:
    print(ValueError)
