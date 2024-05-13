#!/usr/bin/env python
# coding: utf-8

# In[4]:


# H. One Prime
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/H

value = int(input())
if num > 1:
    for i in range(2, (value//2)+1):
        if (value % i) == 0:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")

