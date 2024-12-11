province_list = random.choices(province, k=4)
print("Random province:", province_list)

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
