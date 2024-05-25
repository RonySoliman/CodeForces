#!/usr/bin/env python
# coding: utf-8

# In[3]:


# W. Mathematical Expression
# https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/W

def mathematical_expression(expression):
    expression = expression.replace(" ","")
    
    if "=" in expression:
        operands = expression.split("=")
        left_expr = operands[0]
        right_value = int(operands[1])
        
        # Evaluate the left side of the equation
        result = eval(left_expr)
        
        # Compare the result
        return "Yes" if result == right_value else result
    
    else:
    # define operator and operands
        if "+" in expression:
            operands = expression.split("+")
            operator = "+"
        elif "-" in expression:
            operands = expression.split("-")
            operator = "-"
        elif "*" in expression:
            operands = expression.split("*")
            operator = "*"
        elif "=" in expression:
            operands = expression.split("=")
            operator = "="

    
    A = int(operands[0])
    B = int(operands[1])
    C = int(operands[2])
    
    #perform the operation
    if operator == "+":
        result = (A+B) == C
    elif operator == "-":
        result = (A-B) == C
    elif operator == "*":
        result = (A*B) == C
    elif operator == "=":
        result = A == B
        
    return "Yes" if result==C else print(result)

#Example usage:
expression = input().strip()
print(mathematical_expression(expression))

