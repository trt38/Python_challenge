# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 14:52:29 2020

@author: T
"""

import os
import csv

poll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    total_votes = 0 
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0   
    
    candidates = []
    
    for rows in csvreader: 
        total_votes = total_votes+1 
               
        if rows[2] == "Khan": 
            khan_votes = khan_votes+1
            
        elif rows[2] == "Correy":
            correy_votes = correy_votes+1
            
        elif rows[2] == "Li": 
            li_votes = li_votes+1
            
        elif rows[2] == "O'Tooley":
            otooley_votes = otooley_votes+1
            
khan_perc = khan_votes / total_votes
correy_perc = correy_votes / total_votes
li_perc = li_votes / total_votes
otooley_perc = otooley_votes / total_votes

winnercount = max(khan_votes, correy_votes, li_votes, otooley_votes)
if(winnercount == khan_votes):
    winner = "Khan" 
elif(winnercount == correy_votes):
    winner = "Correy"
elif(winnercount == li_votes):
    winner = "Li"
else:
    winner = "O'Tooley"
            
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("Khan: " + "{:.3%}".format(khan_perc) + " " + "(" + str(khan_votes) + ")")
print("Correy: " + "{:.3%}".format(correy_perc) + " " + "(" + str(correy_votes) + ")")
print("Li: " + "{:.3%}".format(li_perc) + " " + "(" + str(li_votes) + ")")
print("O'Tooley': " + "{:.3%}".format(otooley_perc) + " " + "(" + str(otooley_votes) + ")")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")
 

election_output = os.path.join("PyPoll", "Resources", "election_summary.txt")

with open(election_output, "w") as file:
    
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write("Total Votes: " + str(total_votes))
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write("Khan: " + "{:.3%}".format(khan_perc) + " " + "(" + str(khan_votes) + ")")
    file.write("\n")
    file.write("Correy: " + "{:.3%}".format(correy_perc) + " " + "(" + str(correy_votes) + ")")
    file.write("\n")
    file.write("Li: " + "{:.3%}".format(li_perc) + " " + "(" + str(li_votes) + ")")
    file.write("\n")
    file.write("O'Tooley': " + "{:.3%}".format(otooley_perc) + " " + "(" + str(otooley_votes) + ")")
    file.write("\n")
    file.write("-------------------------")
    file.write("Winner: " + str(winner))
    file.write("\n")
    file.write("-------------------------")
