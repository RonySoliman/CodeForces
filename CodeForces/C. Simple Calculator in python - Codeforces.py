#!/usr/bin/env python
# coding: utf-8

# In[6]:


# C. Simple Calculator
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/C

#how I approach this task!
values = list(map(int,input().split()))

for i in values:
    summ = values[0]+values[1]
    multi = values[0]*values[1]
    sub = values[0]-values[1]
    
    print(f"{values[0]} + {values[1]} = {summ}")
    print(f"{values[0]} * {values[1]} = {multi}")
    print(f"{values[0]} - {values[1]} = {sub}")
    break


# In[ ]:





# In[ ]:




