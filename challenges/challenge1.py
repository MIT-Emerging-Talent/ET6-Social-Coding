# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 1: Detecting Suspicious Login Attempts
Objective:
The goal of this challenge is to practice Boolean algebra simplification. Students will write a Python program to simplify a
given Boolean expressions using Boolean Algebra’s law, helping them understand how to optimize logical expressions in 
programming.
Scenario:
A cybersecurity team is investigating an authentication system that occasionally flags legitimate login attempts as 
suspicious. The system checks multiple conditions to determine if a login attempt should be blocked.
One of the core checks involves the following rule:
¬(A∧(B∨¬B))
where:
A: The user has provided the correct login credentials.
B: The login attempt is from a trusted device.
The security team suspects that the system might be blocking users incorrectly due to redundant logic checks. Your task is
to simplify the logic to understand what the system is actually doing and determine if the rule is valid or needs 
modification.

Task:
Analyze the given Boolean expression.
Apply Boolean law to simplify it.
Interpret what the final expression means in the context of allowing or blocking a login attempt.

"""

A=bool()
B=bool()
SecurityCheck=bool()

# Simplifying 
# not(A and(B or not(B)))= not(A and 1)=not(A)

SecurityCheck = not(A) 

if SecurityCheck:
    print ('Login incorrect. Please enter valid login')
else: print ('Login correct.')


#Interpretation: User hasn't provided correct login credentials


def simplify_expression(A, B):
    # Original expression: ¬(A ∧ (B ∨ ¬B))
    # Step 1: Simplify (B ∨ ¬B) to True
    inner_expression = True  # Since B ∨ ¬B is always True
    # Step 2: Simplify A ∧ True to A
    intermediate_expression = A and inner_expression  # A ∧ True = A
    # Step 3: Apply the negation
    final_expression = not intermediate_expression  # ¬A
    return final_expression

# Example usage:
A = True  # User has correct credentials
B = True  # Login attempt is from a trusted device

result = simplify_expression(A, B)
print(f"The simplified expression evaluates to: {result}")