import csv
with open('student.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(reader)
    for row in reader:
        print(row)
    # for row in reader:
    #     roll = row['RollNo']
    #     name =row['Name']
    #     marks = float(row['marks'])
    #
    #     if roll not in students:
