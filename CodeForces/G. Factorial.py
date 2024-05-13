#!/usr/bin/env python
# coding: utf-8

# In[8]:


# G. Factorial
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/G

value1 = int(input())
value2 = int(input())
value3 = int(input())
start1 = 1
start2 = 1
for i in range(1,value2+1):
    start1 = start1*i
for j in range(1,value3+1):
    start2=start2*j
    
print(start1)
print(start2)

