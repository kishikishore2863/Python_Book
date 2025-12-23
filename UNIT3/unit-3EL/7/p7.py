try:
    with open("t7.txt", 'r') as inFile:
        output = []
        lines = inFile.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                num = int(line)
                output.append(str(line))
            except ValueError:
                print("Invalid number line",line)
    with open('outputFile.txt', 'w') as f:
        for i in output:
               f.write(i+"\n")
except Exception as e:
    print(e)