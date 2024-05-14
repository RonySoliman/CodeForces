#!/usr/bin/env python
# coding: utf-8

# In[6]:


# D. Difference
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/D

values = list(map(int,input().split()))

for i in values:
    cal = (values[0]*values[1]) - (values[2]*values[3])
    print(f"Difference = {cal}")
    break

