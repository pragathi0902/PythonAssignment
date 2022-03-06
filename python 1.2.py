# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 19:19:09 2022

@author: praga
"""

print("1.Add")
print("2.Subtract")
a=int(input("Enter the option "))
v1=int(input("Enter the value 1: "))
v2=int(input("Enter the value 2: "))
if (a==1):
    print ("Output:",v1+v2)
else:
    print ("Output:",v1-v2)
a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
if(a>b)and(a>c):
    print("a is greater")
elif(b>a)and(b>c):
    print("b is greater")
else:
    print("c is greater")

if(a%5==0 or a%10==0):
    print("number is either multiple of 5 or 10")
else:
    print("number is neither multiple of 5 nor 10")
    
if(a != 10):
    print("number is 10")
    
