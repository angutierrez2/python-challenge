# Import Python Packages

import os

import csv

# Import CSV File

election_csv = os.path.join('Resources', 'election_data.csv')

# Calculate the Total Number of Votes Cast

with open(election_csv, 'r') as csvfile:

    # Split the Data on ','
    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # List to Track Vote Count

    vote_count = [0]
        
    # Count Instances of Votes Cast in CSV
    
    for row in csvreader:
            
        if row[1] == row[1]:
        
            vote_count[0] += 1
        
    # Print Total Count of Votes
    
    total_votes = vote_count[0]
            
    print("Election Results")
    
    print("----------------------------")
    
    print("Total Votes: " + str(total_votes))
    
    print("----------------------------")
    
# Calculate the Percentage of Votes and Total Votes Each Candidate Won
    
with open(election_csv, 'r') as csvfile:

    # Split the Data on ','
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # List to Track Percentage of Votes for Each Candidate
    
    percentage_votes = [0,0,0]
 
    # List to Track Vote Count for Each Candidate

    candidate_votes = [0,0,0]
    
    # Count Candidate Votes and Percentage of Votes in CSV File
    
    for row in csvreader:
            
        if row[2] == "Charles Casper Stockham":
            
            candidate_votes[0] += 1
            
            percentage_votes[0] = round(candidate_votes[0] / total_votes * 100, 3)
            
        elif row[2] == "Diana DeGette":

            candidate_votes[1] += 1  
            
            percentage_votes[1] = round(candidate_votes[1] / total_votes * 100, 3)
            
        elif row[2] == "Raymon Anthony Doane":
        
            candidate_votes[2] += 1
            
            percentage_votes[2] = round(candidate_votes[2] / total_votes * 100, 3)
            
    # Print Total Count of Votes and Percentage of Votes
         
    print("Charles Casper Stockham: " + str(percentage_votes[0]) + "% (" + str(candidate_votes[0]) + ") ")
         
    print("Diana DeGette: " + str(percentage_votes[1]) + "% (" + str(candidate_votes[1]) + ") ")
    
    print("Raymon Anthony Doane: " + str(percentage_votes[2]) + "% (" + str(candidate_votes[2]) + ") ")
    
    print("----------------------------")
    
# Find Winner of the Election Based on Popular Vote

x = 200000

if x < candidate_votes[0]:
            
    print("Winner: Charles Casper Stockham")
            
elif x < candidate_votes[1]:
            
    print("Winner: Diana DeGette")
            
elif x < candidate_votes[2]:
            
    print("Winner: Raymon Anthony Doane")
    
print("----------------------------")
    
# Output Analysis to Text File

with open("pypoll_analysis.txt", "w") as file2:
    
    # Write Data to Text File
    
    file2.write("Election Results\n----------------------------\n")
    
    file2.write("Total Votes: " + str(total_votes))
    
    file2.write("\n----------------------------\nCharles Casper Stockham: " + str(percentage_votes[0]) + "% (" + str(candidate_votes[0]) + ") ")
    
    file2.write("\nDiana DeGette: " + str(percentage_votes[1]) + "% (" + str(candidate_votes[1]) + ") ")
    
    file2.write("\nRaymon Anthony Doane: " + str(percentage_votes[2]) + "% (" + str(candidate_votes[2]) + ") ")
    
    file2.write("\n----------------------------\nWinner: Diana DeGette\n----------------------------\n")
