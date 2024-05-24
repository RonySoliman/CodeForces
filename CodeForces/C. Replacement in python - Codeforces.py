#!/usr/bin/env python
# coding: utf-8

# In[8]:


# C. Replacement
# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/C

def checker(list_input):
    #list_input = list_input.replace('[','').replace(']','')
    for value in range(len(list_input)):
        if list_input[value] > 0:
            list_input[value] = 1
        elif list_input[value] < 0:
            list_input[value] = 2
        elif list_input[value] == 0:
            list_input[value] = 0
    return list_input

number_of_items = int(input())
list_input = list(map(int,input().split()))

result = checker(list_input)
#print(result)

# Print the transformed array without brackets
print(" ".join(map(str, result)))

