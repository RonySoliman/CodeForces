#!/usr/bin/env python
# coding: utf-8

# In[2]:


# C. Even, Odd, Positive and Negative
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/C

values = input()
checker = list(map(int, input().split()))
 
for i in range(len(checker)):
    Even,Odd,Positive,Negative=0,0,0,0
 
    for i in checker:
        if (int(i)%2==0):
            Even+=1
        else: 
            Odd+=1
        if (int(i)>0):
            Positive+=1
        else:
            Negative+=1
 
    print(f"Even: {Even}") #
    print(f"Odd: {Odd}") # -5 0 -3 -4 12
    print(f"Positive: {Positive}") #correct
    print(f"Negative: {Negative}") #
    
    break

