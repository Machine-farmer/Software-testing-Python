#!/usr/bin/env python3

import csv

# Prepare data for new file
new_data = []

# Read data from the original file and append to new_data
with open('mock_data_copy.csv', 'r') as f:
    csv_f = csv.reader(f)
    next(csv_f)  # Skip the header row of the original file
    for row in csv_f:
        id, f_name, l_name, email, gender, ip_address = row
        print("Name: {}, Gender: {}, Email: {}".format(f_name+" "+ l_name, gender, email))
        # Append new row to new_data
        name = f_name + " " + l_name
        new_data.append([name, email])

# Define the header
header = ['Name', 'Email']

# Write new_data to new file
with open('new_mock_data_copy.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    writer.writerows(new_data)  # Write the data