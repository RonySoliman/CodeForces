#!/usr/bin/env python
# coding: utf-8

# In[11]:


# A. Boy or Girl
# https://codeforces.com/problemset/problem/236/A

value = str(input())

for i in value:
    if (len(set(value))%2) == 0: #set() used to get iteratable unique values 
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
    break

#don't count repeated char wjmzbmr = count as 6 as (m) is repeated twice!

