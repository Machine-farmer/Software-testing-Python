#!/usr/bin/env python3
with open("README.md", "r") as file:
    print(file.readline())
    print("Newline after first readline\n")
    print(file.readline())
    print("Newline after second readline and before first read method\n")
    print(file.read())

with open("README.md", "r+") as file:
    for line in file:
        print(line.strip().upper())