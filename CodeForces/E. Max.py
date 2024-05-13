#!/usr/bin/env python
# coding: utf-8

# In[2]:


# E. Max
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/E

num = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    print(max(numbers))
    break
    
# https://stackoverflow.com/questions/29811082/how-to-print-out-a-numbered-list-in-python-3

