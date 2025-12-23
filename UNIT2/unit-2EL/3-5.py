#A Conference class stores venue_name as a class variable.
# Each session has a speaker and duration. A class method updates venue_name.
# A static method validates duration.
# Print details to verify the class variable change.

class Conference:
    venue_name = "City Hall"

    def __init__(self, speaker, duration):
        self.speaker = speaker
        self.duration = duration

    @classmethod
    def update_venue(cls, new_venue):
        cls.venue_name = new_venue

    @staticmethod
    def is_valid_duration(d):
        return d > 0

s1 = Conference("Dr. Rao", 60)
s2 = Conference("Prof. Mehta", 45)
s3 = Conference("Ms. Anita", 30)

print(s1.speaker, s1.duration, Conference.venue_name, Conference.is_valid_duration(s1.duration))
print(s2.speaker, s2.duration, Conference.venue_name, Conference.is_valid_duration(s2.duration))
print(s3.speaker, s3.duration, Conference.venue_name, Conference.is_valid_duration(s3.duration))

Conference.update_venue("National Convention Center")

print(s1.speaker, s1.duration, Conference.venue_name)
print(s2.speaker, s2.duration, Conference.venue_name)
print(s3.speaker, s3.duration, Conference.venue_name)