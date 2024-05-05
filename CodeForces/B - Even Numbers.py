#!/usr/bin/env python
# coding: utf-8

# In[ ]:


intputt = int(input())

for inputt in range(2,1000):
    for i in range(1,intputt+1):
        if (i%2 == 0):
            print(i)
    if i == 1:
        print(-1)
    break

