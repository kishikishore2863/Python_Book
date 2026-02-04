import csv
li=[
    [6,'suraj',25],
    [7,'suraj',25],
    [8,'suraj',25],
    [9,'suraj',25]
]
with open('demo.csv','a+',newline='')as f:
    writer= csv.writer(f)
    writer.writerows(li)