# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
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
"""
import matplotlib.pyplot as plt 
from matplotlib_venn import venn2

finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}

tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}

admin={"E0001"}

new_employee={"E9999"}

venn_values = (finance_access, tech_access, admin, new_employee)
venn_labels = ('Finance', 'Tech', 'Admin', 'New employee')

venn=venn2(subsets=venn_values, set_labels=venn_labels)
plt.show()

"""

from matplotlib_venn import venn2
import matplotlib.pyplot as plt

finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
admin = {"E0001"}
new_employee = {"E9999"}

#Venn diagram
venn2(subsets=(len(finance_access - tech_access),
               len(tech_access - finance_access),
               len(finance_access.intersection(tech_access))),
      set_labels=("Finance Access", "Tech Access"))

# For adding title and colors
plt.title("Employee Access Control Visualization")
plt.annotate("Admin: Full Access", xy=(-0.6, -0.5))
plt.annotate("New Employee: No Access", xy=(-0.6, -0.6))
plt.show()

