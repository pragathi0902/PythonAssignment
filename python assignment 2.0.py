# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:01:31 2022

@author: praga
"""

#1
l1=[22,33,44]
l1[0]=55
print(l1)

l1={1:22,2:33,3:44}
l1[1]=55
print(l1)

#2
#append
a=[1,2,3,4,5]
a.append(6)
print(a)
#copy
b=a.copy()
print(b)
#count
print(a.count(4))
#extend
b=[7,8,9]
a.extend(b)
print(a)
#index
print(a.index(1))
#insert
a.insert(0,0)
print(a)
#reverse
a.reverse()
print(a)
#sort
a.sort()
print(a)
#pop
print(a.pop())
#remove
a.remove(1)
print(a)
#clear
a.clear()
print(a)

#3
#copy
a={1:'one',2:'two',3:'three'}
b=a.copy()
print(b)
#fromkeys
key={"list","tuple"}
value="python"
d=dict.fromkeys(key,value)
print(d)
#get
print(a.get(1))
#items
print(a.items())
#keys
print(a.keys())
#pop
a.pop(3)
print(a)
#popitem
print(a.popitem())
#setdefault
a.setdefault(3,"three")
print(a)
#update
b={4:"four"}
a.update(b)
print(a)
#value
print(a.values())
#clear
a.clear()
print(a)

#4
str = "methods"
print(str.capitalize())
newString = "NewValue"
print(newString.casefold())
print(newString.center(2,'a'))
print(newString.count('e'))
print(newString.encode())
print(newString.endswith('e'))
print(newString.expandtabs(2))
print(newString.find('w'))
txt="For only {price:.2f} dollars"
print(txt.format(price=49))
a={'x':'John','y':'wick'}
print("{x}'s last name is {y}".format_map(a))
print(newString.index('a'))
print(newString.isalnum())
print(newString.isalpha())
print(newString.isascii())
print(newString.isdecimal())
print(newString.isdigit())
print(newString.isidentifier())
print(newString.islower())
print(newString.isnumeric())
print(newString.isprintable())
print(newString.isspace())
print(newString.istitle())
print(newString.isupper())
print(newString.rfind('a'))
print(newString.rindex('a'))
print(newString.rjust(1))
print(newString.rpartition('new'))
print(newString.rsplit())
print(newString.rstrip())
print(newString.swapcase())
print(newString.title())
print(newString.translate('e'))
print(newString.upper())
print(newString.zfill(0))