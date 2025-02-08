# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

Group name: Salle 8
Group members: Dadi Ishimwe
              Robel Mengsteab
              Safa Saber
              Louis Kervens Hubert
              M Jawid Mohseni
              Mohamed El - nageeb
              Franklyn Abanihe
              Mariia Ermishina


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

# 1 - finance_access OR tech_access
at_least_one = finance_access | tech_access

# 2 - Team = finance_access AND tech_access 
both_access = finance_access & tech_access

# 3 - finance_access_exclusive {"E0435", "E1021", "E3098"}  
exclusive_finance = finance_access - tech_access

# 3 - tech_access_exclusive {"E9812", "E4520"}
exclusive_tech = tech_access - finance_access

# 4 - no_access = new_employee E9999
all_employees = {"E0001", "E9999", "E0435", "E1021", "E3098", "E7642", "E8873", "E6590", "E9812", "E4520"}
no_access = all_employees - (finance_access | tech_access)

# 5 - overlap_risk = finance_access AND tech_access
overlap = finance_access & tech_access

# The should not share common dates and Grant employees only the access they absolutely need to perform their job duties.
