class InvalidAgeException(Exception):
    "raised when the input value is less than 18"
    pass

number =18

try:
    input_num = int(input("Enter a number: "))
    if input_num > number:
        print("Eligible to vote")
    else:
        raise InvalidAgeException

except InvalidAgeException:
    print("Exception occurred: invalid Age")