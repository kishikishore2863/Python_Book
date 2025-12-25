import csv
import pandas as pd

FILENAME = "data.csv"


# -------------------------------
# 1. CREATE / WRITE CSV
# -------------------------------
def create_csv():
    data = [
        ["id", "name", "age"],
        [1, "Kishore", 22],
        [2, "Ravi", 24],
        [3, "Neha", 21]
    ]
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("CSV created")


# -------------------------------
# 2. READ CSV
# -------------------------------
def read_csv():
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# -------------------------------
# 3. READ CSV AS DICTIONARY
# -------------------------------
def read_csv_dict():
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


# -------------------------------
# 4. APPEND TO CSV
# -------------------------------
def append_csv():
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([4, "Amit", 26])
    print("Row appended")


# -------------------------------
# 5. UPDATE CSV
# -------------------------------
def update_csv(update_id, new_age):
    rows = []
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == str(update_id):
                row[2] = str(new_age)
            rows.append(row)

    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("CSV updated")


# -------------------------------
# 6. DELETE ROW
# -------------------------------
def delete_row(delete_id):
    rows = []
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] != str(delete_id):
                rows.append(row)

    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Row deleted")


# -------------------------------
# 7. SEARCH IN CSV
# -------------------------------
def search_csv(name):
    with open(FILENAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["name"] == name:
                print("Found:", row)
                return
    print("Not found")


# -------------------------------
# 8. COUNT ROWS
# -------------------------------
def count_rows():
    with open(FILENAME) as f:
        count = sum(1 for _ in f) - 1
    print("Total rows:", count)


# -------------------------------
# 9. SORT CSV BY AGE
# -------------------------------
def sort_csv():
    with open(FILENAME, "r") as f:
        rows = list(csv.reader(f))

    header = rows[0]
    data = rows[1:]
    data.sort(key=lambda x: int(x[2]))

    with open("sorted.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([header] + data)

    print("CSV sorted -> sorted.csv")


# -------------------------------
# 10. CSV USING PANDAS
# -------------------------------
def pandas_ops():
    df = pd.read_csv(FILENAME)
    print(df)

    # update
    df.loc[df["id"] == 2, "age"] = 30

    # delete
    df = df[df["id"] != 3]

    # save
    df.to_csv("pandas_out.csv", index=False)
    print("Pandas operations done")


# -------------------------------
# MAIN EXECUTION
# -------------------------------
if __name__ == "__main__":
    create_csv()
    read_csv()
    append_csv()
    update_csv(1, 23)
    delete_row(3)
    search_csv("Kishore")
    count_rows()
    sort_csv()
    pandas_ops()