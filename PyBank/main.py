print("Financial Analysis")
print("--------------------------")
import os
import csv

PyBank_csv = os.path.join("budget_data.csv")

# Number of Months
#with open(PyBank_csv, newline="") as csvfile:
 #   next(csvfile)
  #  csvreader = csv.reader(csvfile, delimiter=",")
   # month = list(csvreader)
    #row_count = len(month)
    #print("Total Months: " + str(row_count))

# Net total amount of "Profit/Losses"
with open(PyBank_csv, newline="") as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    month = []
    revenue = []
    for row in csvreader:
        revenue.append(float(row[1]))
        month.append(row[0])
    print("Total Months: ", len(month))
    print("Total: $",int(sum(revenue)))


with open(PyBank_csv, newline="") as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")

    rev_change = []
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = sum(rev_change)/len(rev_change) 
    print("Average Change: $", round(avg_rev_change, 2))

    max_rev_change = max(rev_change)
    min_rev_change = min(rev_change)


    max_rev_change_date = str(month[rev_change.index(max(rev_change))+1])
    min_rev_change_date = str(month[rev_change.index(min(rev_change))+1])

    print("Greatest Increase in Profits:", max_rev_change_date,"($", round(max_rev_change),")")
    print("Greatest Decrease in Profits:", min_rev_change_date,"($", round(min_rev_change),")")

    
import sys
sys.stdout = open("PyBank_output.txt", "w")
print("Financial Analysis")
print("--------------------------")
print("Total Months: ", len(month))
print("Total: $",int(sum(revenue)))
print("Average Change: $", round(avg_rev_change, 2))
print("Greatest Increase in Profits:", max_rev_change_date,"($", round(max_rev_change),")")
print("Greatest Decrease in Profits:", min_rev_change_date,"($", round(min_rev_change),")")
