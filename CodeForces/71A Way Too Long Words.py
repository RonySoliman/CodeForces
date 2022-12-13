#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input()) 
i = 1 
while(i <= n): 
    word = str(input()) 
    if len(word) > 10: 
        print(f"{word[0]}{len(word) - 2}{word[-1]}") 
    else: 
        print(word) 
    i+=1


# In[ ]:




