#!/usr/bin/env python
# coding: utf-8

# In[57]:


# R. Age in Days
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/R

def convert_age_in_days(N):
    # Calculate years
    years = N // 365
    remaining_days = N % 365
    
    # Calculate months
    months = remaining_days // 30
    days = remaining_days % 30
    
    # Print the results
    print(f"{years} years")
    print(f"{months} months")
    print(f"{days} days")

# Example usage:
N = int(input())  # Example input
convert_age_in_days(N)

