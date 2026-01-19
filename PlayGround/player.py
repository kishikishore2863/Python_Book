class InvalidAgeError(Exception):
    "kishikihsore"
    pass
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age is below 18")
    print(f"Age {age} is valid.")

try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Error: {e}")
