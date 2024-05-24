#!/usr/bin/env python
# coding: utf-8

# In[5]:


# A. Summation
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/A

number = int(input())
values = list(map(int,input().split()))

for value in values:
    result = abs(sum(values))
    print(result)
    break

