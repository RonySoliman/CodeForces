#!/usr/bin/env python
# coding: utf-8

# In[2]:


# F. Multiplication table
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/F

value = int(input())

for value in range(1,50):
    if (int(value) >=1) & (int(value)<13):
        print(f"{value} * {value} = {value*value}")
        


# In[6]:


number = int(input())
for i in range(1,13):
    print(f"{number} * {i} = {number*i}")


# In[5]:


number = int(input())
for number in range(1,50):
    for i in range(1,13):
        print(f"{number} * {i} = {number*i}")

