# the user inputs any positive integer 
# and outputs the successive values of the following calculation.

# The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows:

# If the previous term is even,the next term is half of the previous term.
# If the previous term is odd,the next term is 3 times the previous term plus 1.
# The conjecture is that no matter what value of n, the sequence will always reach 1.

# if x is odd,then next term 3*x + 1
# if x is even,then next term x//2

# Author Sinead McCormack


def collatz (number):
    if number % 2 ==0:
        return number //2
    elif number % 2 ==1:
        return 3 * number +1
    
number = int(input("Please enter a positive Number: "))

while number !=1:
    collatz(number)
    number = collatz(number)
    print(number, end= ' ')
  



   

















         
