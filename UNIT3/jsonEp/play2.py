try:
    filename = input("Enter file name to create: ")

    with open(filename, "w") as file:
        data = input("Enter text to write into the file: ")
        file.write(data)

    print("File created and data written successfully.")

except PermissionError:
    print("Permission denied: You do not have permission to create this file.")

except Exception as e:
    print("An error occurred:", e)