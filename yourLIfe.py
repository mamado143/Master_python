year_of_birth = int(input("What year were you born? "))
age = 2023 - year_of_birth
months = age * 12
weeks = age * 52
days = age * 365
hours = age * 8760
minutes = age * 525600
seconds = age * 31536000
print(f"You are {age} years old.")
print(f"You are {months} months old.")
print(f"You are {weeks} weeks old.")
print(f"You are {days} days old.")
print(f"You are {hours} hours old.")
print(f"You are {minutes} minutes old.")
print(f"You are {seconds} seconds old.")

# yourLife.py