#11. Create check_strength(password) that checks: ≥8 characters at least one uppercase, lowercase, digit, and special character Return “Strong” or “Weak”.
def check_strength(password):
    if (len(password) >= 8 and
        any(ch.isupper() for ch in password) and
        any(ch.islower() for ch in password) and
        any(ch.isdigit() for ch in password) and
        any(ch in "!@#$%^&*()_+" for ch in password)):
        return "Strong"
    return "Weak"

print(check_strength("Abc@1234"))

