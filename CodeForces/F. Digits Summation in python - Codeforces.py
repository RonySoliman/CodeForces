#!/usr/bin/env python
# coding: utf-8

# In[1]:


# F. Digits Summation
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/F

values = list(map(int,input().split()))
#print(values)

for value in values:
    cal = sum(value%10 for value in values)
    print(cal)
    break
    
# Link:
# https://stackoverflow.com/questions/17626552/add-the-last-digits-in-a-number-list-in-python


# In Python, the % operator is called the modulo operator. It returns the remainder of the division of the left operand by the right operand. So, value % 10 in Python would give you the remainder when value is divided by 10. This operation is commonly used to extract the last digit of a number or to perform operations that depend on cycling through a fixed range of numbers, such as 0 to 9.
