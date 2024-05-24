#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Q. Coordinates of a Point
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Q

values = list(map(float,input().split()))

def Coordinates_Point(X,Y):
    if (values[0] == 0) & (values[1] == 0):
        return "Origem"
    elif (values[0] == 0):
        return "Eixo Y"
    elif (values[1] == 0):
        return "Eixo X"
    elif (values[0] >= 0) & (values[1] >= 0):
        return "Q1"
    elif (values[0] < 0) & (values[1] >= 0):
        return "Q2"
    elif (values[0] < 0) & (values[1] < 0):
        return "Q3"
    elif (values[0] >= 0) & (values[1] < 0):
        return "Q4"

if __name__ == '__main__':
    X = values[0]
    Y = values[1]
    
    output = Coordinates_Point(values[0],values[1])
    print(output)

