import csv

with open('expenses.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Store", "Date", "Total Amount","Added Date"])