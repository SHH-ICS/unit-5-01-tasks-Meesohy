# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
from math import sqrt
word= str()
word= input ("Welcome! Click enter!")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("Length of hypotenuse is:", c )
