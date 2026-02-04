try:
    with open('marks.txt','r')as file:
        # for i in file:
        #     print(i.strip())
        read = file.readlines()
        max = 0
        for i in read:
            max +=int(i.strip('\n'))

        print(read)
        print(max)
except Exception as e:
    print(e)