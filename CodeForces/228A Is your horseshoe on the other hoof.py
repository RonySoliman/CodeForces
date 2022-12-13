#!/usr/bin/env python
# coding: utf-8

# In[6]:


# the correct answer:

s = list(map(int, input().split()))

sol = []

for color in s:
    if color not in sol:
        sol.append(color)
        
print(4 - len(sol))


# In[ ]:





# In[ ]:





# In[ ]:




