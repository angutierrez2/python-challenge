# Import Python Packages

import os

import csv

# Import CSV File

budget_csv = os.path.join('Resources', 'budget_data.csv')

# Calculate Total Number of Months Included in Datasheet

with open(budget_csv, 'r') as csvfile:

    # Split the Data on '-'
    
    csvreader = csv.reader(csvfile, delimiter='-')

    header = next(csvreader)

    # List to Track Start Count

    start_count = [0]

    # Month List
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Display Initial Message

    print("Financial Analysis")

    print("----------------------------")
        
    # Count Instances of Months in CSV File
    
    for row in csvreader:
        
        if month_list[0] == row[0]:
        
            start_count[0] += 1
            
        elif month_list[1] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[2] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[3] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[4] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[5] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[6] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[7] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[8] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[9] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[10] == row[0]:
            
            start_count[0] += 1
            
        elif month_list[11] == row[0]:
            
            start_count[0] += 1
        
    # Print Month Count
    
    month_count = start_count[0]
            
    print("Total Months: " + str(month_count))

# Calculate Net Total Amount of Profit/Losses Over Entire Period

with open(budget_csv, 'r') as csvfile:

    # Split the Data on ','
    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # List to Track Start Amount

    start_amount = [0]
        
    # Count Instances of Amounts of Profit/Losses in CSV File
    
    x = 12000000
    
    for row in csvreader:
        
        if x > int(row[1]) :
        
            start_amount[0] += int(row[1])
        
    # Print Total Profit/Losses
    
    total_amount = start_amount[0]
            
    print("Total: $" + str(total_amount))
