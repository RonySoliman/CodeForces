#!/usr/bin/env python
# coding: utf-8

# In[9]:


# B. Searching
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/B

# 3 "the items in the list"
# 3 0 1 "the list"
# 0 "the value I will look for in the list"

number_of_items = int(input())
list_input = list(map(int,input().split()))
value = int(input())

if value in list_input:
    print(list_input.index(value)) #to locate the index
else:
    print(-1)

