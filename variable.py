#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:33:37 2024

@author: mac
"""

a  = 100
b  = 100.00
c = 'Lab'
age = [10,30,60,90,80]
name = ['aliyu','joseph','umar']
people = ('aliyu','joseph','umar')
student = {"name": "pofi", "address": "anguwan Rukuba", "age": 20}
students = [{"name": "pofi", "address": "anguwan Rukuba", "age": 20},{"name": "musa", "address": "anguwan rugu", "age": 25}]

print(type(a))
#<class 'int'>
print(type(b))
#<class 'float'>
print(type(c))
#<class 'str'>
print(type(age))
#<class 'list'>
print(type(people))
#<class 'tuple'>
print(type(student))
#<class 'dict'>

print(name)
#['aliyu', 'joseph', 'umar']
name[0] = "jone"
print(name)
#['jone', 'joseph', 'umar']


print(people)
#('aliyu', 'joseph', 'umar')
print(student)
#{'name': 'pofi', 'address': 'anguwan Rukuba', 'age': 20}
print(student["name"])
#pofi
print(students[0]["name"])
#pofi
print(students[1]["name"])
#musa