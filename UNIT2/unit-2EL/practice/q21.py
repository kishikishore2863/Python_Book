import csv

with open('demo.csv','r')as f:
    # read = csv.reader(f)
    # for r in read:
    #     print(r)

    dic_read = csv.DictReader(f)
    print(type(dic_read))
    for d in dic_read:
        print(d)
