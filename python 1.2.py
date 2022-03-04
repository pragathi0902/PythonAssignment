# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 19:19:09 2022

@author: praga
"""

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
    