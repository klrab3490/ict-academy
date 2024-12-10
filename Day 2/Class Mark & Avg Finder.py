'''
A class of n students with m subjects to study

app: 
 - add student mark
 - each sudent average and subject average

'''

class5 = []

# Input number of students
stud_count = int(input("Enter No. of students in the class: "))
subject_count = int(input("Enter No. of subject to be taken by each student: "))

# Collect marks for each student in each subject
for i in range(stud_count):
    sub_mark = []  # to store marks of a student in all subjects
    print(f"Student {i+1}:")
    for j in range(subject_count):  # Loop through 5 subjects
        mark = int(input(f"Enter Mark for Subject {j+1}: "))
        sub_mark.append(mark)
    class5.append(sub_mark)
    print()

# Printing the class data
print("Class Data: ")
for i in range(stud_count):
    print(f"Student {i+1}: {class5[i]}")

# Calculate subject averages
avg_mark = []
for j in range(subject_count):  # Loop through 5 subjects
    total_marks = 0
    for i in range(stud_count):
        total_marks += class5[i][j]
    avg_mark.append(total_marks / stud_count)

# Calculate student averages
avg_stud = []
for i in range(stud_count):
    total_marks = 0
    for j in range(subject_count):  # Loop through 5 subjects
        total_marks += class5[i][j]
    avg_stud.append(total_marks / subject_count)  # Divide by number of subjects

# Print averages
print("\nSubject Averages: ", avg_mark)
print("Student Averages: ", avg_stud)
