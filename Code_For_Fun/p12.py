#12. Given a seed value of 5. Generate a password that is of 10 characters. At least one uppercase, lowercase, digit, and special character.
import random
import string

random.seed(5)
chars = string.ascii_letters + string.digits + "!@#$%^&*()"

password = []
password.append(random.choice(string.ascii_uppercase))
password.append(random.choice(string.ascii_lowercase))
password.append(random.choice(string.digits))
password.append(random.choice("!@#$%^&*()"))

password += random.choices(chars, k=6)
random.shuffle(password)

print("Generated Password:", ''.join(password))


