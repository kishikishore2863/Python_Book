#A Subscription class stores default_duration as a class variable.
# Each subscription object stores user_name and start_date.
# A class method updates default_duration.
# A static method checks if the start date format is valid.
# Print durations before and after the update.


class Subscription:
    default_duration = 12

    def __init__(self, user_name, start_date):
        self.user_name = user_name
        self.start_date = start_date

    @classmethod
    def update_duration(cls, months):
        cls.default_duration = months

    @staticmethod
    def is_valid_date(date_str):
        parts = date_str.split("-")
        return len(parts) == 3 and all(p.isdigit() for p in parts)

s1 = Subscription("Kishore", "2025-01-01")
s2 = Subscription("Amit", "2024-12-10")

print(s1.user_name, s1.start_date, Subscription.default_duration, Subscription.is_valid_date(s1.start_date))
print(s2.user_name, s2.start_date, Subscription.default_duration, Subscription.is_valid_date(s2.start_date))

Subscription.update_duration(24)

print(s1.user_name, s1.start_date, Subscription.default_duration)
print(s2.user_name, s2.start_date, Subscription.default_duration)