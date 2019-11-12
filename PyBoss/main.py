import os
import csv
employee_csv = os.path.join("employee_data.csv")
Emp_ID = []
Name = []
DOB = []
SSN = []
State = []
First_Name = []
Last_Name = []
SSN1 = []
SSN2 = []
SSN3 = []

with open(employee_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        Emp_ID.append(row[0])
        Name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        State.append(row[4])
        New_Name1= row[1].split(" ")
        New_Name2= row[1].split(" ")
        First_Name.append(New_Name1[0])
        Last_Name.append(New_Name2[1])
        First_Name.append(New_Name1[0])
        Last_Name.append(New_Name2[1])
cleaned_csv = zip(Emp_ID,  First_Name, Last_Name, DOB, SSN, State)
output_file = os.path.join("PyBoss_Revised.csv")
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile) 
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])
    writer.writerows(cleaned_csv)
