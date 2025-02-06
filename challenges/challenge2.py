# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 2: Digital Access Control
Objective
Use set operations to analyze and improve a company's digital access control system while identifying potential security risks in data access.
Scenario
A secure company vault stores sensitive data, where employees are granted access based on their roles:
Finance Team (F): Needs access to financial records.
Tech Team (T): Needs access to technical documents.
Some employees belong to both teams due to cross-departmental responsibilities.
Access Data (Given)
The security system tracks employee IDs (formatted as "E####").
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
Additionally, two special cases exist:
E0001 (Admin): Has access to all data but is not listed in specific access groups.
E9999 (New Employee): Has no assigned access yet.
Your Task
Analyze the current access structure and identify potential security risks by answering the following:
Who has access to at least one type of data?
Who has access to both financial and technical data?
Who has exclusive access to only one type of data?
Which employees currently lack access (but exist in the system)?
Are there unnecessary overlaps in access that could pose a security risk?
What changes would you recommend to enhance security and minimize excessive access?
# -*- coding: utf-8 -*-

"""
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}

tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}

admin={"E0001"}

new_employee={"E9999"}

#Who has access to at least one type of data?
Access_One_type=finance_access.union(tech_access).union(admin)

#Who has access to both financial and technical data?
Access_both_types=finance_access.intersection(tech_access).union(admin)

#Who has exclusive access to only one type of data?
Access_one_type_only=finance_access.symmetric_difference(tech_access)
print (Access_one_type_only)

#Which employees currently lack access (but exist in the system)?
print ("New employee has no access!", new_employee)

#Are there unnecessary overlaps in access that could pose a security risk?
print("Access to both types is an unnecessary intersection.", Access_both_types) 

#What changes would you recommend to enhance security and minimize excessive access?
print("Security Recommendations: Restrict access according to the roles and responsibilities")




