# program that reads in two numbers and 
# outputs the integer ansewer and reminder

x = int(input ("Enter your first number: "))
y = int(input ("Enter your second number: "))
answer = int (x//y) # // which give int diviision
remainder = x%y # % which gives the remainder 

print("{} divided by {} is {} with the remainder {}" .format (x, y, answer, remainder))
