#hw3 PyPoll

#imports
import os
import csv

#variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#set Path for file
csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')

#open and read csv
with open(csvpath, newline='') as csvfile:

    #Delimiter and variable for content
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    #read the header row first
    csv_header = next(csvfile)

    #read each row after the header
    for row in csv_reader:

        #calculate total Num of votes 
        total_votes += 1

        #calculate number of votes per candidate
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

    #calculate Percentage of votes per candidate
    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

    #calculate winner of election
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"    
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name: "O'Tooley"

#Print Analysis
print(f"Election Results")
print(f"--------------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------------")
print(f"Khan: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"--------------------------------")
print(f"Winner: {winner_name}")
print(f"--------------------------------")

#specifiy file to write
output_file = os.path.join('.', 'PyPoll', 'Resources', 'election_data_revised.text')

#open file using write mode for the variables to hold content
with open(output_file, 'w',) as txtfile:

    #write new data
    txtfile.write(f"Election Results")
    txtfile.write(f"--------------------------------")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write(f"--------------------------------")
    txtfile.write(f"Khan: {kahn_percent:.3%}({khan_votes})")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
    txtfile.write(f"--------------------------------")
    txtfile.write(f"Winner: {winner_name}")
    txtfile.write(f"--------------------------------")
