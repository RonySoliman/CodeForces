#!/usr/bin/env python
# coding: utf-8

# In[19]:


# J. Multiples
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/J

values = list(map(int,input().split()))

if ((values[0]%values[1]) == 0) or ((values[1]%values[0]) == 0):
    print("Multiples")
else:
    print("No Multiples")

