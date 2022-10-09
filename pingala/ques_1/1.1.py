import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,simplify

x=symbols('x')
y=symbols('y')
t=symbols('t')

def a(n):
  return (x**n-y**n)/(x-y)

l=0
for i in range(1,6):
  l+=a(i)
print(simplify(l))
if(l==a(5+2)-1):
  print("true")
else:
  print("false")