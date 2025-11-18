#Use zip() and max() to find the student with the highest score from two parallel lists.
students = ["Kishore", "Rahul", "Sneha", "Meena"]
marks = [89, 76, 92, 85]

# Pair students with marks using zip
combined = list(zip(students, marks))

# Find the student with highest score
top_student = max(combined, key=lambda x: x[1])

print(top_student)