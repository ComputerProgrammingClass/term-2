"""
students = []


def add_student(name, age):
    students.append({name: name, age: age})


add_student("Jason", 11)
add_student("Jeff", 12)
add_student("Jessica", "12")
add_student("Julia", 13)
"""

# Second code, sampling with replacement
list = [20, 30, 40, 50, 60, 70, 80]
sampling = random.choices(list, k=4)
print("Randomly selected multiple choices using random.choices() ", sampling)

import random

funny_list = random.sample(range(10, 30), 21)
print(funny_list)

for x in range(27):
    if z % 2 == 0:
        continue
    print(y)
