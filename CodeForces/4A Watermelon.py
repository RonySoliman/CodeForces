#!/usr/bin/env python
# coding: utf-8

# In[11]:


w = int(input())

if (w > 0) & (w in range(1,101)) & (int(w%2 == 0)) & (w!=2):
    print("YES")
    
else:
    print("NO")    


# In[ ]:




