# program that prints out a random number between 1 and 10

import random

number = random.randint(1, 10)
print("here is the ramdom number: {} ".format(number))



x = int(input("Enter the number of Random no. Display = "))
start_Val = int("Enter the first value = ")
end_Val = int("Enter the last value = ")
for i in range (0, x):
print(random.randint(start_Val, end_Val))


