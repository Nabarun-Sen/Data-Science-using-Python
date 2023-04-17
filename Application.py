import sys
sys.path.append("C:\Code")
import Function as fun
b=int(input("Enter base: "))
h=int(input("Enter height: "))
l=int(input("Enter length: "))
print("Area of Square")
print(fun.square_area(l))
print("Area of Triangle")
print(fun.triangle_area(b,h))