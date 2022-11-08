import csv
csv_columns = ['No','Name','Country']
dict_data = [
{'No': 1, 'Name': 'jay', 'Country': 'India'},
{'No': 2, 'Name': 'Bean', 'Country': 'USA'},
{'No': 3, 'Name': 'sagar', 'Country': 'India'},
{'No': 4, 'Name': 'Smith', 'Country': 'USA'},
{'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
]
csv_file = "Names.csv"



try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
            
except IOError:
    print("I/O error")
