students=[
    {'name' : 'alice','scores':{'math':80,'science':90}},
    {'name':'Bob','scores':{'math':70,'science':85}},
    {'name':'charlie','scores':{'math':90,'science':95}}
]

squaered_scores ={
    student['name']:{subject:score**2 for subject,score in student ['scores'].items()}
    for student in students
}

print(squaered_scores)



filterted_table ={
    i:{j:i*j for j in range(1,6) if(i*j)%2 == 0} for i in range(1,6)
}

print(filterted_table)