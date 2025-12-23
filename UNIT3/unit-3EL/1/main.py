with open("text.txt", "r") as f:
    for line in f:
        line = line.strip()
        try:
            num = int(line)
            print("Converted:", num)
        except ValueError:
            print("ValueError → cannot convert:", line)
               
