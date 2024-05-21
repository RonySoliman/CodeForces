#!/usr/bin/env python
# coding: utf-8

# In[31]:


# O. Calculator
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/O

def evaluate_expression(expression):
    # Remove spaces from the expression
    expression = expression.replace(" ", "")
    
    # Find the operator and operands
    if '+' in expression:
        operands = expression.split('+')
        operator = '+'
    elif '-' in expression:
        operands = expression.split('-')
        operator = '-'
    elif '*' in expression:
        operands = expression.split('*')
        operator = '*'
    elif '/' in expression:
        operands = expression.split('/')
        operator = '/'
    else:
        return "Invalid expression"

    # Convert operands to float (or int if you prefer)
    A = int(operands[0])
    B = int(operands[1])
    
    # Perform the operation
    if operator == '+':
        result = A + B
    elif operator == '-':
        result = A - B
    elif operator == '*':
        result = A * B
    elif operator == '/':
        if B == 0:
            return "Error: Division by zero"
        result = int(A / B)
    
    return result

# Example usage:
expression = input()
print(evaluate_expression(expression))  # Output: 19.8

