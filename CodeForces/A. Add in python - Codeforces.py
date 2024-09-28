#!/usr/bin/env python
# coding: utf-8

# In[12]:


import time
value = list(map(int,input().split()))

a = time.time()
def add(values):
    
    for x,y in enumerate(values):
        res = sum(values)
        print(res)
        break
add(value)
b = time.time()
print(b-a)


# In[13]:


value = list(map(int, input().split()))
c = time.time()
def add(values):
    res = sum(values)  # Sum the entire list directly
    print(res)

add(value)  # Call the function with the input list
d = time.time()
print(d-c)

