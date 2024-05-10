#!/usr/bin/env python
# coding: utf-8

# In[2]:


# E. Max
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/E

values = int(input())
checker = list(map(int, input().split()))

for values in range(1,1000):
    for i,j in enumerate(checker):
        num = max(checker)
    print(num)
    break
    
# https://stackoverflow.com/questions/29811082/how-to-print-out-a-numbered-list-in-python-3

