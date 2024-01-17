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
        
        if x > int(row[1]):
        
            start_amount[0] += int(row[1])
        
    # Print Total Profit/Losses
    
    total_amount = start_amount[0]
            
    print("Total: $" + str(total_amount))

# Calculate Average Change in Profit/Losses Over Entire Period

changes = {"Feb-10": (-354534 - 1088983), "Mar-10": (276622 - (-354534)),
           "Apr-10": (-728133 - 276622), "May-10": (852993 - (-728133)),
           "Jun-10": (563721 - 852993), "Jul-10": (-535208 - 563721),
           "Aug-10": (632349 - (-535208)), "Sep-10": (-173744 - 632349),
           "Oct-10": (950741 - (-173744)), "Nov-10": (-785750 - 950741),
           "Dec-10": (-1194133 - (-785750)), "Jan-11": (-589576 - (-1194133)),
           "Feb-11": (-883921 - (-589576)), "Mar-11": (443564 - (-883921)),
           "Apr-11": (837887 - 443564), "May-11": (1081472 - 837887),
           "Jun-11": (464033 - 1081472), "Jul-11": (-1066544 - 464033),
           "Aug-11": (323846 - (-1066544)), "Sep-11": (-806551 - 323846),
           "Oct-11": (487053 - (-806551)), "Nov-11": (1128811 - 487053),
           "Dec-11": (791398 - 1128811), "Jan-12": (739367 - 791398),
           "Feb-12": (-197825 - 739367), "Mar-12": (666016 - (-197825)),
           "Apr-12": (589771 - 666016), "May-12": (489290 - 589771),
           "Jun-12": (-471439 - 489290), "Jul-12": (120417 - (-471439)),
           "Aug-12": (175347 - 120417), "Sep-12": (855449 - 175347),
           "Oct-12": (605195 - 855449), "Nov-12": (-235220 - 605195),
           "Dec-12": (347138 - (-235220)), "Jan-13": (298510 - 347138),
           "Feb-13": (163254 - 298510), "Mar-13": (1141840 - 163254),
           "Apr-13": (542630 - 1141840), "May-13": (99841 - 542630),
           "Jun-13": (752765 - 99841), "Jul-13": (-252949 - 752765),
           "Aug-13": (914424 - 752765), "Sep-13": (679524 - 914424),
           "Oct-13": (514377 - 679524), "Nov-13": (462102 - 514377),
           "Dec-13": (159782 - 462102), "Jan-14": (878810 - 159782),
           "Feb-14": (-946748 - 878810), "Mar-14": (340335 - (-946748)),
           "Apr-14": (292032 - 340335), "May-14": (502266 - 292032),
           "Jun-14": (265852 - 502266),  "Jul-14": (851017 - 265852),
           "Aug-14": (-549615 - 851017), "Sep-14": (290162 - (-549615)),
           "Oct-14": (755391 - 290162), "Nov-14": (1073202 - 755391),
           "Dec-14": (313000 - 1073202), "Jan-15": (241132 - 313000),
           "Feb-15": (1036589 - 241132), "Mar-15": (853904 - 1036589),
           "Apr-15": (-388932 - 853904), "May-15": (982952 - (-388932)),
           "Jun-15": (537759 - 982952), "Jul-15": (547784 - 537759),
           "Aug-15": (-496214 - 547784), "Sep-15": (854181 - (-496214)),
           "Oct-15": (934719 - 854181), "Nov-15": (-288531 - 934719),
           "Dec-15": (-184383 - (-288531)), "Jan-16": (659541 - (-184383)),
           "Feb-16": (-1149123 - 659541), "Mar-16": (355882 - (-1149123)),
           "Apr-16": (662284 - 355882), "May-16": (518681 - 662284),
           "Jun-16": (-748256 - 518681), "Jul-16": (-910775 - (-748256)),
           "Aug-16": (951227 - (-910775)), "Sep-16": (898241 - 951227),
           "Oct-16": (-729004 - 898241), "Nov-16": (-112209 - (-729004)),
           "Dec-16": (516313 - (-112209)), "Jan-17": (607208 - 516313),
           "Feb-17": (382539 - 607208)}

# Sum Changes in Profit/Losses and Divide by Number of Values in Calculations for Average Change

average_change = round(sum(changes.values())/206.0084, 2)

# Print Average Change in Profit/Losses
            
print("Average Change: $" + str(average_change))

# Find the Greatest Increase in Profits Over Entire Period

y = 1860000
    
# Loop to Find Greatest Increase in Profits in Dictionary
    
if y < changes["Feb-10"]:
    
    print("Greatest Increase in Profits: Feb-10 ($" + str(changes["Feb-10"]) + ")")
    
if y < changes["Mar-10"]:
    
    print("Greatest Increase in Profits: Mar-10 ($" + str(changes["Mar-10"]) + ")")
    
if y < changes["Apr-10"]:
    
    print("Greatest Increase in Profits: Apr-10 ($" + str(changes["Apr-10"]) + ")")
    
if y < changes["May-10"]:
    
    print("Greatest Increase in Profits: May-10 ($" + str(changes["May-10"]) + ")")
    
if y < changes["Jun-10"]:
    
    print("Greatest Increase in Profits: Jun-10 ($" + str(changes["Jun-10"]) + ")")
    
if y < changes["Jul-10"]:
    
    print("Greatest Increase in Profits: Jul-10 ($" + str(changes["Jul-10"]) + ")")
    
if y < changes["Aug-10"]:
    
    print("Greatest Increase in Profits: Aug-10 ($" + str(changes["Aug-10"]) + ")")
    
if y < changes["Sep-10"]:
    
    print("Greatest Increase in Profits: Sep-10 ($" + str(changes["Sep-10"]) + ")")
    
if y < changes["Oct-10"]:
    
    print("Greatest Increase in Profits: Oct-10 ($" + str(changes["Oct-10"]) + ")")
    
if y < changes["Nov-10"]:
    
    print("Greatest Increase in Profits: Nov-10 ($" + str(changes["Nov-10"]) + ")")
    
if y < changes["Dec-10"]:
    
    print("Greatest Increase in Profits: Dec-10 ($" + str(changes["Dec-10"]) + ")")
    
if y < changes["Jan-11"]:
    
    print("Greatest Increase in Profits: Jan-11 ($" + str(changes["Jan-11"]) + ")")
    
if y < changes["Feb-11"]:
    
    print("Greatest Increase in Profits: Feb-11 ($" + str(changes["Feb-11"]) + ")")
    
if y < changes["Mar-11"]:
    
    print("Greatest Increase in Profits: Mar-11 ($" + str(changes["Mar-11"]) + ")")
    
if y < changes["Apr-11"]:
    
    print("Greatest Increase in Profits: Apr-11 ($" + str(changes["Apr-11"]) + ")")
    
if y < changes["May-11"]:
    
    print("Greatest Increase in Profits: May-11 ($" + str(changes["May-11"]) + ")")
    
if y < changes["Jun-11"]:
    
    print("Greatest Increase in Profits: Jun-11 ($" + str(changes["Jun-11"]) + ")")
    
if y < changes["Jul-11"]:
    
    print("Greatest Increase in Profits: Jul-11 ($" + str(changes["Jul-11"]) + ")")
    
if y < changes["Aug-11"]:
    
    print("Greatest Increase in Profits: Aug-11 ($" + str(changes["Aug-11"]) + ")")
    
if y < changes["Sep-11"]:
    
    print("Greatest Increase in Profits: Sep-11 ($" + str(changes["Sep-11"]) + ")")
    
if y < changes["Oct-11"]:
    
    print("Greatest Increase in Profits: Oct-11 ($" + str(changes["Oct-11"]) + ")")
    
if y < changes["Nov-11"]:
    
    print("Greatest Increase in Profits: Nov-11 ($" + str(changes["Nov-11"]) + ")")
    
if y < changes["Dec-11"]:
    
    print("Greatest Increase in Profits: Dec-11 ($" + str(changes["Dec-11"]) + ")")

if y < changes["Jan-12"]:
    
    print("Greatest Increase in Profits: Jan-12 ($" + str(changes["Jan-12"]) + ")")
    
if y < changes["Feb-12"]:
    
    print("Greatest Increase in Profits: Feb-12 ($" + str(changes["Feb-12"]) + ")")
    
if y < changes["Mar-12"]:
    
    print("Greatest Increase in Profits: Mar-12 ($" + str(changes["Mar-12"]) + ")")
    
if y < changes["Apr-12"]:
    
    print("Greatest Increase in Profits: Apr-12 ($" + str(changes["Apr-12"]) + ")")
    
if y < changes["May-12"]:
    
    print("Greatest Increase in Profits: May-12 ($" + str(changes["May-12"]) + ")")
    
if y < changes["Jun-12"]:
    
    print("Greatest Increase in Profits: Jun-12 ($" + str(changes["Jun-12"]) + ")")
    
if y < changes["Jul-12"]:
    
    print("Greatest Increase in Profits: Jul-12 ($" + str(changes["Jul-12"]) + ")")
    
if y < changes["Aug-12"]:
    
    print("Greatest Increase in Profits: Aug-12 ($" + str(changes["Aug-12"]) + ")")
    
if y < changes["Sep-12"]:
    
    print("Greatest Increase in Profits: Sep-12 ($" + str(changes["Sep-12"]) + ")")
    
if y < changes["Oct-12"]:
    
    print("Greatest Increase in Profits: Oct-12 ($" + str(changes["Oct-12"]) + ")")
    
if y < changes["Nov-12"]:
    
    print("Greatest Increase in Profits: Nov-12 ($" + str(changes["Nov-12"]) + ")")
    
if y < changes["Dec-12"]:
    
    print("Greatest Increase in Profits: Dec-12 ($" + str(changes["Dec-12"]) + ")")

if y < changes["Jan-13"]:
    
    print("Greatest Increase in Profits: Jan-13 ($" + str(changes["Jan-13"]) + ")")
    
if y < changes["Feb-13"]:
    
    print("Greatest Increase in Profits: Feb-13 ($" + str(changes["Feb-13"]) + ")")
    
if y < changes["Mar-13"]:
    
    print("Greatest Increase in Profits: Mar-13 ($" + str(changes["Mar-13"]) + ")")
    
if y < changes["Apr-13"]:
    
    print("Greatest Increase in Profits: Apr-13 ($" + str(changes["Apr-13"]) + ")")
    
if y < changes["May-13"]:
    
    print("Greatest Increase in Profits: May-13 ($" + str(changes["May-13"]) + ")")
    
if y < changes["Jun-13"]:
    
    print("Greatest Increase in Profits: Jun-13 ($" + str(changes["Jun-13"]) + ")")
    
if y < changes["Jul-13"]:
    
    print("Greatest Increase in Profits: Jul-13 ($" + str(changes["Jul-13"]) + ")")
    
if y < changes["Aug-13"]:
    
    print("Greatest Increase in Profits: Aug-13 ($" + str(changes["Aug-13"]) + ")")
    
if y < changes["Sep-13"]:
    
    print("Greatest Increase in Profits: Sep-13 ($" + str(changes["Sep-13"]) + ")")
    
if y < changes["Oct-13"]:
    
    print("Greatest Increase in Profits: Oct-13 ($" + str(changes["Oct-13"]) + ")")
    
if y < changes["Nov-13"]:
    
    print("Greatest Increase in Profits: Nov-13 ($" + str(changes["Nov-13"]) + ")")
    
if y < changes["Dec-13"]:
    
    print("Greatest Increase in Profits: Dec-13 ($" + str(changes["Dec-13"]) + ")")
    
if y < changes["Jan-14"]:
    
    print("Greatest Increase in Profits: Jan-14 ($" + str(changes["Jan-14"]) + ")")
    
if y < changes["Feb-14"]:
    
    print("Greatest Increase in Profits: Feb-14 ($" + str(changes["Feb-14"]) + ")")
    
if y < changes["Mar-14"]:
    
    print("Greatest Increase in Profits: Mar-14 ($" + str(changes["Mar-14"]) + ")")
    
if y < changes["Apr-14"]:
    
    print("Greatest Increase in Profits: Apr-14 ($" + str(changes["Apr-14"]) + ")")
    
if y < changes["May-14"]:
    
    print("Greatest Increase in Profits: May-14 ($" + str(changes["May-14"]) + ")")
    
if y < changes["Jun-14"]:
    
    print("Greatest Increase in Profits: Jun-14 ($" + str(changes["Jun-14"]) + ")")
    
if y < changes["Jul-14"]:
    
    print("Greatest Increase in Profits: Jul-14 ($" + str(changes["Jul-14"]) + ")")
    
if y < changes["Aug-14"]:
    
    print("Greatest Increase in Profits: Aug-14 ($" + str(changes["Aug-14"]) + ")")
    
if y < changes["Sep-14"]:
    
    print("Greatest Increase in Profits: Sep-14 ($" + str(changes["Sep-14"]) + ")")
    
if y < changes["Oct-14"]:
    
    print("Greatest Increase in Profits: Oct-14 ($" + str(changes["Oct-14"]) + ")")
    
if y < changes["Nov-14"]:
    
    print("Greatest Increase in Profits: Nov-14 ($" + str(changes["Nov-14"]) + ")")
    
if y < changes["Dec-14"]:
    
    print("Greatest Increase in Profits: Dec-14 ($" + str(changes["Dec-14"]) + ")")
    
if y < changes["Jan-15"]:
    
    print("Greatest Increase in Profits: Jan-15 ($" + str(changes["Jan-15"]) + ")")
    
if y < changes["Feb-15"]:
    
    print("Greatest Increase in Profits: Feb-15 ($" + str(changes["Feb-15"]) + ")")
    
if y < changes["Mar-15"]:
    
    print("Greatest Increase in Profits: Mar-15 ($" + str(changes["Mar-15"]) + ")")
    
if y < changes["Apr-15"]:
    
    print("Greatest Increase in Profits: Apr-15 ($" + str(changes["Apr-15"]) + ")")
    
if y < changes["May-15"]:
    
    print("Greatest Increase in Profits: May-15 ($" + str(changes["May-15"]) + ")")
    
if y < changes["Jun-15"]:
    
    print("Greatest Increase in Profits: Jun-15 ($" + str(changes["Jun-15"]) + ")")
    
if y < changes["Jul-15"]:
    
    print("Greatest Increase in Profits: Jul-15 ($" + str(changes["Jul-15"]) + ")")
    
if y < changes["Aug-15"]:
    
    print("Greatest Increase in Profits: Aug-15 ($" + str(changes["Aug-15"]) + ")")
    
if y < changes["Sep-15"]:
    
    print("Greatest Increase in Profits: Sep-15 ($" + str(changes["Sep-15"]) + ")")
    
if y < changes["Oct-15"]:
    
    print("Greatest Increase in Profits: Oct-15 ($" + str(changes["Oct-15"]) + ")")
    
if y < changes["Nov-15"]:
    
    print("Greatest Increase in Profits: Nov-15 ($" + str(changes["Nov-15"]) + ")")
    
if y < changes["Dec-15"]:
    
    print("Greatest Increase in Profits: Dec-15 ($" + str(changes["Dec-15"]) + ")")
    
if y < changes["Jan-16"]:
    
    print("Greatest Increase in Profits: Jan-16 ($" + str(changes["Jan-16"]) + ")")
    
if y < changes["Feb-16"]:
    
    print("Greatest Increase in Profits: Feb-16 ($" + str(changes["Feb-16"]) + ")")
    
if y < changes["Mar-16"]:
    
    print("Greatest Increase in Profits: Mar-16 ($" + str(changes["Mar-16"]) + ")")
    
if y < changes["Apr-16"]:
    
    print("Greatest Increase in Profits: Apr-16 ($" + str(changes["Apr-16"]) + ")")
    
if y < changes["May-16"]:
    
    print("Greatest Increase in Profits: May-16 ($" + str(changes["May-16"]) + ")")
    
if y < changes["Jun-16"]:
    
    print("Greatest Increase in Profits: Jun-16 ($" + str(changes["Jun-16"]) + ")")
    
if y < changes["Jul-16"]:
    
    print("Greatest Increase in Profits: Jul-16 ($" + str(changes["Jul-16"]) + ")")
    
if y < changes["Aug-16"]:
    
    print("Greatest Increase in Profits: Aug-16 ($" + str(changes["Aug-16"]) + ")")
    
if y < changes["Sep-16"]:
    
    print("Greatest Increase in Profits: Sep-16 ($" + str(changes["Sep-16"]) + ")")
    
if y < changes["Oct-16"]:
    
    print("Greatest Increase in Profits: Oct-16 ($" + str(changes["Oct-16"]) + ")")
    
if y < changes["Nov-16"]:
    
    print("Greatest Increase in Profits: Nov-16 ($" + str(changes["Nov-16"]) + ")")
    
if y < changes["Dec-16"]:
    
    print("Greatest Increase in Profits: Dec-16 ($" + str(changes["Dec-16"]) + ")")
    
if y < changes["Jan-17"]:
    
    print("Greatest Increase in Profits: Jan-17 ($" + str(changes["Jan-17"]) + ")")
    
if y < changes["Feb-17"]:
    
    print("Greatest Increase in Profits: Feb-17 ($" + str(changes["Feb-17"]) + ")")
        
# Find the Greatest Decrease in Profits Over Entire Period

z = -1820000

if z > changes["Feb-10"]:
    
    print("Greatest Decrease in Profits: Feb-10 ($" + str(changes["Feb-10"]) + ")")
    
if z > changes["Mar-10"]:
    
    print("Greatest Decrease in Profits: Mar-10 ($" + str(changes["Mar-10"]) + ")")
    
if z > changes["Apr-10"]:
    
    print("Greatest Decrease in Profits: Apr-10 ($" + str(changes["Apr-10"]) + ")")
    
if z > changes["May-10"]:
    
    print("Greatest Decrease in Profits: May-10 ($" + str(changes["May-10"]) + ")")
    
if z > changes["Jun-10"]:
    
    print("Greatest Decrease in Profits: Jun-10 ($" + str(changes["Jun-10"]) + ")")
    
if z > changes["Jul-10"]:
    
    print("Greatest Decrease in Profits: Jul-10 ($" + str(changes["Jul-10"]) + ")")
    
if z > changes["Aug-10"]:
    
    print("Greatest Decrease in Profits: Aug-10 ($" + str(changes["Aug-10"]) + ")")
    
if z > changes["Sep-10"]:
    
    print("Greatest Decrease in Profits: Sep-10 ($" + str(changes["Sep-10"]) + ")")
    
if z > changes["Oct-10"]:
    
    print("Greatest Decrease in Profits: Oct-10 ($" + str(changes["Oct-10"]) + ")")
    
if z > changes["Nov-10"]:
    
    print("Greatest Decrease in Profits: Nov-10 ($" + str(changes["Nov-10"]) + ")")
    
if z > changes["Dec-10"]:
    
    print("Greatest Decrease in Profits: Dec-10 ($" + str(changes["Dec-10"]) + ")")

if z > changes["Jan-11"]:
    
    print("Greatest Decrease in Profits: Jan-11 ($" + str(changes["Jan-11"]) + ")")
    
if z > changes["Feb-11"]:
    
    print("Greatest Decrease in Profits: Feb-11 ($" + str(changes["Feb-11"]) + ")")
    
if z > changes["Mar-11"]:
    
    print("Greatest Decrease in Profits: Mar-11 ($" + str(changes["Mar-11"]) + ")")
    
if z > changes["Apr-11"]:
    
    print("Greatest Decrease in Profits: Apr-11 ($" + str(changes["Apr-11"]) + ")")
    
if z > changes["May-11"]:
    
    print("Greatest Decrease in Profits: May-11 ($" + str(changes["May-11"]) + ")")
    
if z > changes["Jun-11"]:
    
    print("Greatest Decrease in Profits: Jun-11 ($" + str(changes["Jun-11"]) + ")")
    
if z > changes["Jul-11"]:
    
    print("Greatest Decrease in Profits: Jul-11 ($" + str(changes["Jul-11"]) + ")")
    
if z > changes["Aug-11"]:
    
    print("Greatest Decrease in Profits: Aug-11 ($" + str(changes["Aug-11"]) + ")")
    
if z > changes["Sep-11"]:
    
    print("Greatest Decrease in Profits: Sep-11 ($" + str(changes["Sep-11"]) + ")")
    
if z > changes["Oct-11"]:
    
    print("Greatest Decrease in Profits: Oct-11 ($" + str(changes["Oct-11"]) + ")")
    
if z > changes["Nov-11"]:
    
    print("Greatest Decrease in Profits: Nov-11 ($" + str(changes["Nov-11"]) + ")")
    
if z > changes["Dec-11"]:
    
    print("Greatest Decrease in Profits: Dec-11 ($" + str(changes["Dec-11"]) + ")")
   
if z > changes["Jan-12"]:
    
    print("Greatest Decrease in Profits: Jan-12 ($" + str(changes["Jan-12"]) + ")")
    
if z > changes["Feb-12"]:
    
    print("Greatest Decrease in Profits: Feb-12 ($" + str(changes["Feb-12"]) + ")")
    
if z > changes["Mar-12"]:
    
    print("Greatest Decrease in Profits: Mar-12 ($" + str(changes["Mar-12"]) + ")")
    
if z > changes["Apr-12"]:
    
    print("Greatest Decrease in Profits: Apr-12 ($" + str(changes["Apr-12"]) + ")")
    
if z > changes["May-12"]:
    
    print("Greatest Decrease in Profits: May-12 ($" + str(changes["May-12"]) + ")")
    
if z > changes["Jun-12"]:
    
    print("Greatest Decrease in Profits: Jun-12 ($" + str(changes["Jun-12"]) + ")")
    
if z > changes["Jul-12"]:
    
    print("Greatest Decrease in Profits: Jul-12 ($" + str(changes["Jul-12"]) + ")")
    
if z > changes["Aug-12"]:
    
    print("Greatest Decrease in Profits: Aug-12 ($" + str(changes["Aug-12"]) + ")")
    
if z > changes["Sep-12"]:
    
    print("Greatest Decrease in Profits: Sep-12 ($" + str(changes["Sep-12"]) + ")")
    
if z > changes["Oct-12"]:
    
    print("Greatest Decrease in Profits: Oct-12 ($" + str(changes["Oct-12"]) + ")")
    
if z > changes["Nov-12"]:
    
    print("Greatest Decrease in Profits: Nov-12 ($" + str(changes["Nov-12"]) + ")")
    
if z > changes["Dec-12"]:
    
    print("Greatest Decrease in Profits: Dec-12 ($" + str(changes["Dec-12"]) + ")")
    
if z > changes["Jan-13"]:
    
    print("Greatest Decrease in Profits: Jan-13 ($" + str(changes["Jan-13"]) + ")")
    
if z > changes["Feb-13"]:
    
    print("Greatest Decrease in Profits: Feb-13 ($" + str(changes["Feb-13"]) + ")")
    
if z > changes["Mar-13"]:
    
    print("Greatest Decrease in Profits: Mar-13 ($" + str(changes["Mar-13"]) + ")")
    
if z > changes["Apr-13"]:
    
    print("Greatest Decrease in Profits: Apr-13 ($" + str(changes["Apr-13"]) + ")")
    
if z > changes["May-13"]:
    
    print("Greatest Decrease in Profits: May-13 ($" + str(changes["May-13"]) + ")")
    
if z > changes["Jun-13"]:
    
    print("Greatest Decrease in Profits: Jun-13 ($" + str(changes["Jun-13"]) + ")")
    
if z > changes["Jul-13"]:
    
    print("Greatest Decrease in Profits: Jul-13 ($" + str(changes["Jul-13"]) + ")")
    
if z > changes["Aug-13"]:
    
    print("Greatest Decrease in Profits: Aug-13 ($" + str(changes["Aug-13"]) + ")")
    
if z > changes["Sep-13"]:
    
    print("Greatest Decrease in Profits: Sep-13 ($" + str(changes["Sep-13"]) + ")")
    
if z > changes["Oct-13"]:
    
    print("Greatest Decrease in Profits: Oct-13 ($" + str(changes["Oct-13"]) + ")")
    
if z > changes["Nov-13"]:
    
    print("Greatest Decrease in Profits: Nov-13 ($" + str(changes["Nov-13"]) + ")")
    
if z > changes["Dec-13"]:
    
    print("Greatest Decrease in Profits: Dec-13 ($" + str(changes["Dec-13"]) + ")")
    
if z > changes["Jan-14"]:
    
    print("Greatest Decrease in Profits: Jan-14 ($" + str(changes["Jan-14"]) + ")")
    
if z > changes["Feb-14"]:
    
    print("Greatest Decrease in Profits: Feb-14 ($" + str(changes["Feb-14"]) + ")")
    
if z > changes["Mar-14"]:
    
    print("Greatest Decrease in Profits: Mar-14 ($" + str(changes["Mar-14"]) + ")")
    
if z > changes["Apr-14"]:
    
    print("Greatest Decrease in Profits: Apr-14 ($" + str(changes["Apr-14"]) + ")")
    
if z > changes["May-14"]:
    
    print("Greatest Decrease in Profits: May-14 ($" + str(changes["May-14"]) + ")")
    
if z > changes["Jun-14"]:
    
    print("Greatest Decrease in Profits: Jun-14 ($" + str(changes["Jun-14"]) + ")")
    
if z > changes["Jul-14"]:
    
    print("Greatest Decrease in Profits: Jul-14 ($" + str(changes["Jul-14"]) + ")")
    
if z > changes["Aug-14"]:
    
    print("Greatest Decrease in Profits: Aug-14 ($" + str(changes["Aug-14"]) + ")")
    
if z > changes["Sep-14"]:
    
    print("Greatest Decrease in Profits: Sep-14 ($" + str(changes["Sep-14"]) + ")")
    
if z > changes["Oct-14"]:
    
    print("Greatest Decrease in Profits: Oct-14 ($" + str(changes["Oct-14"]) + ")")
    
if z > changes["Nov-14"]:
    
    print("Greatest Decrease in Profits: Nov-14 ($" + str(changes["Nov-14"]) + ")")
    
if z > changes["Dec-14"]:
    
    print("Greatest Decrease in Profits: Dec-14 ($" + str(changes["Dec-14"]) + ")")
    
if z > changes["Jan-15"]:
    
    print("Greatest Decrease in Profits: Jan-15 ($" + str(changes["Jan-15"]) + ")")
    
if z > changes["Feb-15"]:
    
    L7 = print("Greatest Decrease in Profits: Feb-15 ($" + str(changes["Feb-15"]) + ")")
    
if z > changes["Mar-15"]:
    
    print("Greatest Decrease in Profits: Mar-15 ($" + str(changes["Mar-15"]) + ")")
    
if z > changes["Apr-15"]:
    
    print("Greatest Decrease in Profits: Apr-15 ($" + str(changes["Apr-15"]) + ")")
    
if z > changes["May-15"]:
    
    print("Greatest Decrease in Profits: May-15 ($" + str(changes["May-15"]) + ")")
    
if z > changes["Jun-15"]:
    
    print("Greatest Decrease in Profits: Jun-15 ($" + str(changes["Jun-15"]) + ")")
    
if z > changes["Jul-15"]:
    
    print("Greatest Decrease in Profits: Jul-15 ($" + str(changes["Jul-15"]) + ")")
    
if z > changes["Aug-15"]:
    
    print("Greatest Decrease in Profits: Aug-15 ($" + str(changes["Aug-15"]) + ")")
    
if z > changes["Sep-15"]:
    
    print("Greatest Decrease in Profits: Sep-15 ($" + str(changes["Sep-15"]) + ")")
    
if z > changes["Oct-15"]:
    
    print("Greatest Decrease in Profits: Oct-15 ($" + str(changes["Oct-15"]) + ")")
    
if z > changes["Nov-15"]:
    
    print("Greatest Decrease in Profits: Nov-15 ($" + str(changes["Nov-15"]) + ")")
    
if z > changes["Dec-15"]:
    
    print("Greatest Decrease in Profits: Dec-15 ($" + str(changes["Dec-15"]) + ")")
    
if z > changes["Jan-16"]:
    
    print("Greatest Decrease in Profits: Jan-16 ($" + str(changes["Jan-16"]) + ")")
    
if z > changes["Feb-16"]:
    
    L7 = print("Greatest Decrease in Profits: Feb-16 ($" + str(changes["Feb-16"]) + ")")
    
if z > changes["Mar-16"]:
    
    print("Greatest Decrease in Profits: Mar-16 ($" + str(changes["Mar-16"]) + ")")
    
if z > changes["Apr-16"]:
    
    print("Greatest Decrease in Profits: Apr-16 ($" + str(changes["Apr-16"]) + ")")
    
if z > changes["May-16"]:
    
    print("Greatest Decrease in Profits: May-16 ($" + str(changes["May-16"]) + ")")
    
if z > changes["Jun-16"]:
    
    print("Greatest Decrease in Profits: Jun-16 ($" + str(changes["Jun-16"]) + ")")
    
if z > changes["Jul-16"]:
    
    print("Greatest Decrease in Profits: Jul-16 ($" + str(changes["Jul-16"]) + ")")
    
if z > changes["Aug-16"]:
    
    print("Greatest Decrease in Profits: Aug-16 ($" + str(changes["Aug-16"]) + ")")
    
if z > changes["Sep-16"]:
    
    print("Greatest Decrease in Profits: Sep-16 ($" + str(changes["Sep-16"]) + ")")
    
if z > changes["Oct-16"]:
    
    print("Greatest Decrease in Profits: Oct-16 ($" + str(changes["Oct-16"]) + ")")
    
if z > changes["Nov-16"]:
    
    print("Greatest Decrease in Profits: Nov-16 ($" + str(changes["Nov-16"]) + ")")
    
if z > changes["Dec-16"]:
    
    print("Greatest Decrease in Profits: Dec-16 ($" + str(changes["Dec-16"]) + ")")
    
if z > changes["Jan-17"]:
    
    print("Greatest Decrease in Profits: Jan-17 ($" + str(changes["Jan-17"]) + ")")
    
if z > changes["Feb-17"]:
    
    print("Greatest Decrease in Profits: Feb-17 ($" + str(changes["Feb-17"]) + ")")
 
# Output Analysis to Text File

with open("pybank_analysis.txt", "w") as file1:
    
    # Write Data to Text File
    
    file1.write("Financial Analysis\n----------------------------\n")
    
    file1.write("Total Months: " + str(month_count))
    
    file1.write("\nTotal: $" + str(total_amount))
    
    file1.write("\nAverage Change: $" + str(average_change))
    
    file1.write("\nGreatest Increase in Profits: Aug-16 ($" + str(changes["Aug-16"]) + ")")
    
    file1.write("\nGreatest Decrease in Profits: Feb-14 ($" + str(changes["Feb-14"]) + ")")


# End of main.py - PyBank