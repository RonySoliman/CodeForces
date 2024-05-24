#!/usr/bin/env python
# coding: utf-8

# In[1]:


# D. Fixed Password
# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/D

def check_password(password):
    return password == "1999"
 
# Read input until the correct password is entered
while True:
    try:
        password = input()
        if check_password(password):
            print("Correct")
            break
        else:
            print("Wrong")
    except EOFError:
        break
