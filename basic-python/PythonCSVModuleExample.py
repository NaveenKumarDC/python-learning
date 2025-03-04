import csv

# Sample data to write into a CSV file
data = [
    ['Name', 'Age'],
    ['Alice', 30],
    ['Bob', 25]
]

# Writing CSV data
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading CSV data
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print("CSV row:", row)
