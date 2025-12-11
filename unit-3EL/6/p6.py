try:
    with open('marks.txt','r') as f:
        lines = f.readlines()
        maximum = 0
        count=0
        for i in lines:
            i = i.strip()
            if not i:
                continue

            try:
                maximum = maximum + int(i)
                count = count + 1
            except ValueError as v:
                print(v)
        if count == 0:
            print(maximum)
        else:
            print(maximum/count)

except Exception as e:
    print(e)
