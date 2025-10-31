import os

if "HOME" in os.environ:
    home_dir = os.environ["HOME"]
    print(f"Your home directory is: {home_dir}")
else:
    print("Environment variable 'HOME' does not exist!")