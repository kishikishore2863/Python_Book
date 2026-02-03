#From a dictionary of employees and salaries, create a dictionary of only those earning more than ₹50,000.
employee ={
    "kishore":100000,
    "Arjun":80000,
    "kane":45000,
    "henry":60000,
    "james":35000
}

# high_salary = { key:value  for key,value in employee.items() if value>50000}
# print(high_salary)

h={k:v for k,v in employee.items() if v>50000}
print(h)