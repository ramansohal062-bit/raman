# Program to find if a number is Armstrong number
 
# Take input from the user
number = int(input("Input your number: "))
 
# Calculate number of digits
digits = len(str(number))
 
# Initialize result variable
resultNumber = 0
 
# find the sum of the a^digits of each digit
temp = number
while temp > 0:
   digit = temp % 10
   resultNumber = resultNumber+digit ** digits
   temp = temp // 10
 
# display the result
if number == resultNumber:
   print(number,"is an Armstrong number")
else:
   print(number, "is not an Armstrong number")
#program to find factors
 
# Goes from 1 to number and checks if I divide the number. If yes, it is a factor


def print_factors(number):
   print("The factors of",number,"are:")
   for i in range(1, number + 1):
       if number % i == 0:
           print(i)
 
# Taking input from the user
number = int(input("Enter your number to find it's factors: "))
 
# Calling our function
print_factors(number)
