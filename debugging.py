students = []
student_count = 0


def add_student(name, age):
    students.append({name: name, age: age})
    student_count += 1


add_student("Jason", 11)
add_student("Jeff", 12)
add_student("Jessica", "12")
add_student("Julia", 13)

print(students)
print(student_count)

"""
# Should print out everything in the list
arr = ["apple", "banana", "cherry", "orange", "starfruit"]
i = 0

while i < len(arr):
    i += 1
    print(arr[i])
"""
