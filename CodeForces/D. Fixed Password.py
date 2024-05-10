#!/usr/bin/env python
# coding: utf-8

# In[1]:


# D. Fixed Password
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/D


value = list(map(int, input().split()))
for i in value:
    if int(i) != 1999:
        print("Wrong")
    else:
        print("Correct")
    continue

