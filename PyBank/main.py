# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:00:00 2020

@author: T
"""

import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    
    months = []
    pandl = []
    pandlchange = []
    
    for rows in csvreader:
        months.append(rows[0])
        pandl.append(int(rows[1]))
        
    for i in range(len(pandl)-1):
         pandlchange.append(pandl[i+1]-pandl[i])
         
    total_months = len(months)
    pandlavg = sum(pandlchange)/len(pandlchange)
    max_increase = max(pandlchange)
    max_decrease = min(pandlchange)
    
print("Financial Analysis")

print("----------------------------")

print("Total Months: " + str(total_months))

print("Total: " + "$" + str(sum(pandl)))

print("Average Change: " + "$" + str(round(pandlavg,2)))

print("Greatest Increase in Profits: " + str(months[pandlchange.index(max(pandlchange))+1]) + " " + "($" + str(max_increase) + ")")

print("Greatest Decrease in Profits: " + str(months[pandlchange.index(min(pandlchange))+1]) + " " + "($" + str(max_decrease) + ")")


budget_output = os.path.join("PyBank", "Analysis", "budget_summary.txt")

with open(budget_output, "w") as file:
    
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Total Months: " + str(total_months))
    file.write("\n")
    file.write("Total: " + "$" + str(sum(pandl)))
    file.write("\n")
    file.write("Average Change: " + "$" + str(round(pandlavg,2)))
    file.write("\n")
    file.write("Greatest Increase in Profits: " + str(months[pandlchange.index(max(pandlchange))+1]) + " " + "($" + str(max_increase) + ")")
    file.write("\n")
    file.write("Greatest Decrease in Profits: " + str(months[pandlchange.index(min(pandlchange))+1]) + " " + "($" + str(max_decrease) + ")")
