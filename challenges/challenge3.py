# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai

Group name: Salle 8
Group members: Dadi Ishimwe
              Robel Mengsteab
              Safa Saber
              Louis Kervens Hubert
              M Jawid Mohseni
              Mohamed El - nageeb
              Franklyn Abanihe
              Mariia Ermishina

Challenge 3: Access Visualization
Objective
Develop a visual representation of the company's access control system to identify patterns, overlaps, and security risks.
Scenario
The company’s security team is struggling to interpret raw access data. They need a clear way to see:
Employees who have access to financial records, technical documents, or both.
Employees with no access, who may need onboarding.
Any overlap that could indicate excessive privileges or security risks.
Instead of listing raw data, your task is to create a structured representation that makes these relationships intuitive and easy to understand.
Your Task
Using the provided employee access data, design a way to illustrate:
Who belongs where? Group employees based on their level of access.
Where is the overlap? Show employees who have access to both financial and technical records.
Who is left out? Identify employees without access.
Are there risks? Indicate employees who might be exposed to unnecessary data.
Your output should visually highlight these relationships without explicitly listing them in a simple table or list. Think beyond just printing data—use a format that helps detect patterns at a glance.
"""
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Employee access data
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
all_employees = {"E0001", "E9999", "E0435", "E1021", "E3098", "E7642", "E8873", "E6590", "E9812", "E4520"}

# Determine employee groups
only_finance = finance_access - tech_access
only_tech = tech_access - finance_access
both_access = finance_access & tech_access
no_access = all_employees - (finance_access | tech_access)

# Create Venn diagram
plt.figure(figsize=(6, 6))
venn = venn2(subsets=(len(only_finance), len(only_tech), len(both_access)), set_labels=("Finance Access", "Tech Access"))
plt.title("Employee Access Visualization")
plt.annotate(f"Employees with no access: {len(no_access)}", xy=(0.5, 0.1), xycoords="axes fraction", ha="center", fontsize=12)
plt.show()
