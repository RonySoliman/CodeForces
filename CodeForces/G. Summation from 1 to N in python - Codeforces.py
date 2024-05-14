#!/usr/bin/env python
# coding: utf-8

# In[19]:


# G. Summation from 1 to N
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/G

value = int(input())
summ = 0

for i in range(1,value+1):
    summ += i
print(summ)

# https://stackoverflow.com/questions/50971279/prints-the-sum-of-the-numbers-1-to-n-in-python


# Another solution...

# In[3]:


# G. Summation from 1 to N
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/G

value = int(input())
print(value*(value+1)//2)

