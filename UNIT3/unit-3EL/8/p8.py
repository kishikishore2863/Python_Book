try:
    with open('file.txt', 'r') as f:
        newVersion=[]
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            arr = line.split()
            if len(arr)!=2:
                continue

            str1 =arr[0]+" "+arr[1]
            newVersion.append(str1)
    with open('newversion.txt', 'w') as newFile:
       for i in newVersion:
           newFile.write(i+"\n")

except ValueError:
    print("invalid amount or category")