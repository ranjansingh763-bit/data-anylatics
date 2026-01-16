import csv
filename = 'students.csv'
students_data = []
total_marks = 0

# 1. Read the CSV file
with open("D:\max\students.csv.csv", mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        marks = float(row['Marks'])
        students_data.append({'name': name, 'marks': marks})
        total_marks += marks

# 2. Find the average marks
average_marks = total_marks / len(students_data)
print(f"Average Marks: {average_marks:.2f}")

# 3. Print names of students who scored above average
print("Students who scored above average:")
for student in students_data:
    if student['marks'] > average_marks:
        print(student['name'])
