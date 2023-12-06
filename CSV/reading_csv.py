#!/usr/bin/env python3
import csv

with open('mock_data_copy.csv', 'r') as f:
    csv_f = csv.reader(f)
    for row in csv_f:
        id, f_name, l_name, email, gender, ip_address = row
        print("Name: {}, Gender: {}, Email: {}".format(f_name+" "+ l_name, gender, email))
