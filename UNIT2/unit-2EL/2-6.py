#A movie class uses a static method to format show timings.
# You must pass multiple timings and verify the formatted output

class Movie:
    @staticmethod
    def format_time(time_24: str) -> str:
        hour, minute = map(int, time_24.split(":"))
        suffix = "AM"
        if hour == 0:
            hour = 12
        elif hour == 12:
            suffix = "PM"
        elif hour > 12:
            hour -= 12
            suffix = "PM"
        return f"{hour}:{minute:02d} {suffix}"

timings = ["09:15", "12:00", "14:45", "18:30", "23:10"]

for t in timings:
    print(f"{t} → {Movie.format_time(t)}")