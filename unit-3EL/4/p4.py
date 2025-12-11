s = "12345"
try:
    number = int(s)
    print("Converted:",number)
except ValueError:
    print("Error:cannot convert to integer. input was:",s)
    