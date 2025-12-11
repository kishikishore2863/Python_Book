try:
    userSearch = input("Find:")
    try:
        with open('t5.txt','r')as f:
            lines = f.readlines()
            found =False
            for idx,line in enumerate(lines,start=1):
                if line.strip() == userSearch.strip():
                    print(f"Found name at line {idx}")
                    found =True
                    break
            if not found:
                raise ValueError("Name not found")
    except FileNotFoundError:
        print("Error: FIle not found!")

    except ValueError as e:
        print(e)
except Exception as e:
    print("Unexpected error:",e)
