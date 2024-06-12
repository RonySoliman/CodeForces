#!/usr/bin/env python
# coding: utf-8

# In[7]:


# A. Bit++
# https://codeforces.com/problemset/problem/282/A

n = int(input())  # Read the number of operations
x = 0  # Initialize x to 0

# Loop n times to read each operation
for _ in range(n):
    operation = input().strip()  # Read and strip any extra whitespace from the operation
    if "++" in operation:  # Check if the operation is an increment
        x += 1
    elif "--" in operation:  # Check if the operation is a decrement
        x -= 1

print(x)  # Output the final value of x

