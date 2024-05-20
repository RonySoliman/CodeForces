#!/usr/bin/env python
# coding: utf-8

# In[3]:


# L. The Brothers
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/L

name1 = list(map(str,input().split()))
name2 = list(map(str,input().split()))

if name1[1] == name2[1]:
    print("ARE Brothers")
else:
    print("NOT")

