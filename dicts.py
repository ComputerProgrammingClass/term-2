# create dictionary of student id -> student name
class_list = {
    1231234: "Matthew Poon",
    4314321: "Matthew Ji",
    6618921: "Matthew Ho",
    3444444: "Matthew Law",
}

# change/add another student
class_list[2222222] = "Matthew Matthew"

# remove a student
class_list.pop(2222222)

# prints out the names of students
print(class_list[1231234])
print(class_list[3444444])

# checks if student number exists in class_list
print(3444444 in class_list)
print(2222222 in class_list)

"""
Output: 

Matthew Poon
Matthew Law
True
False
"""
