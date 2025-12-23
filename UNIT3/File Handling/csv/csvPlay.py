import csv

# with open('data.csv','r') as file:
#     reader = csv.reader(file,skipinitialspace=True)
#     for row in reader:
#         print(row)

with open('data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        for k,v in row.items():
            print(k,"->",end="")
            print(v)

with open('text.txt') as csv_file:
    csv_rader = csv.reader(csv_file)
    line_count =0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in (row[2]).')
            line_count += 1
        print (f'Processed (line_count) lines.')

