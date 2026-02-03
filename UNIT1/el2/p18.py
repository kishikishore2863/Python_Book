#Given two lists — student names and marks — use zip() to display results as tuples.
student = ["kishore","rahul","pallavi","kane"]
marks = [89,76,92,85]

result = list(zip(student,marks))

print(result)

t = tuple([(i,j) for i,j in zip(student,marks)])
print(t)