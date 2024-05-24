#!/usr/bin/env python
# coding: utf-8

# In[8]:


# V. Comparison
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/V

# A < B, A > B, A = B.
#if A=B or 5 > 4 then it's "Right" ... else it's "Wrong"

def evaluate_expression(expression):
    #Remove space from the expression
    expression = expression.replace(" ","")
    
    #Find the operator and operands
    if ">" in expression:
        operands = expression.split(">")
        operator = ">"
    elif "<" in expression:
        operands = expression.split("<")
        operator = "<"
    elif "=" in expression:
        operands = expression.split("=")
        operator = "="
    else:
        return "Invalid Expression!"
    
    A = int(operands[0])
    B = int(operands[1])
    
    #perform the operation
    if operator == ">":
        result = (A>B)
    elif operator == "<":
        result = (A<B)
    elif operator == "=":
        result = (A==B)
    
    return "Right" if result else "Wrong"
    
#Example usage:
expression = input()
print(evaluate_expression(expression))

