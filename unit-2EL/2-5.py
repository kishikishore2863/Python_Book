#A password class uses a static method to check strength rules. You must test five passwords and classify each result.


class Password:
    @staticmethod
    def check_strength(pwd: str) -> str:
        length_ok = len(pwd) >= 8
        upper_ok = any(ch.isupper() for ch in pwd)
        lower_ok = any(ch.islower() for ch in pwd)
        digit_ok = any(ch.isdigit() for ch in pwd)
        special_ok = any(ch in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for ch in pwd)

        if all([length_ok, upper_ok, lower_ok, digit_ok, special_ok]):
            return "Strong"
        elif length_ok and (upper_ok or lower_ok) and digit_ok:
            return "Medium"
        else:
            return "Weak"


# ---- Test 5 passwords ----

passwords = [
    "Kishore123@",   # strong
    "abc123",        # weak
    "HelloWorld",    # medium
    "Pass@1",        # weak
    "Str0ng_Pass!"   # strong
]

for pwd in passwords:
    print(f"{pwd} → {Password.check_strength(pwd)}")