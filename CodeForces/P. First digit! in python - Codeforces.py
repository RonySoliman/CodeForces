#!/usr/bin/env python
# coding: utf-8

# In[18]:


# P. First digit !
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/P

def get_first_digit(num):
    if num < 10:
        return num
    else:
        return get_first_digit(num // 10)

def is_first_digit_even_or_odd(num):
    first_digit = get_first_digit(num)
    if first_digit % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

# Example usage
if __name__ == "__main__":
    num = int(input())
    result = is_first_digit_even_or_odd(num)
    #print(f"The first digit of {num} is {result}.")
    print(result)

