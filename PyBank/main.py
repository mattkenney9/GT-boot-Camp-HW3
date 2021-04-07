#HW3 PyBank

#imports 
import os
import csv

#variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0

#path for file
csvpath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

#read the CSV file
with open(csvpath, newline='') as csvfile:

    #delimiter and variable for content
    csvreader = csv.reader(csvfile, delimiter=',')

    #read header first
    csv_header = next(csvreader)
    row = next(csvreader)

    #calculate number of months, net amount of profit/losses and set variables
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

    #read row of data after the header
    for row in csvreader:

        #calculate total number of months in dataset
        total_months += 1
        #calculate net amount of profit/losses
        net_amount += int(row[1])

        #calculate change over month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        #calculate the greatest increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]

        #calculate the greatest decrease
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]
        
    #calculate the average and the data
    average_change = sum(monthly_change)/len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

#Print Analyst
print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_inc_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_dec_month}, (${lowest})")

#write file
output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')

#open file in the write mode for variables to hold the content
with open(output_file, 'w',) as txtfile:

    #write new data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-----------------------\n")
    txtfile.write(f"Total Months: {total_months}\n") 
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_inc_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_dec_month}, (${lowest})\n")