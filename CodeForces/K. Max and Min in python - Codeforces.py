#!/usr/bin/env python
# coding: utf-8

# In[7]:


# K. Max and Min
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/K

values = list(map(int,input().split()))

for i in values:
    print(min(values),max(values))
    break

