# Quadratic Equation Solver

import math as mt

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))

formula1 = (b + mt.sqrt(b**2 + 4*(a)*(c)))/2*(a)
formula2 = (b - mt.sqrt(b**2 + 4*(a)*(c)))/2*(a)

result1 = formula1
result2 = formula2

final = f"{result1:.2f} , {result2:.2f}"
print(final)