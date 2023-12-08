#!/usr/bin/env python3
import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

print(result.groups())
print(result[0])
print(result[1])
print(result[2])

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))
print(rearrange_name("Voltaire"))

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Kennedy, John F."))
print(rearrange_name("Hopper, Grace M."))

print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.findall(r"s\w{,20}", "I really like strawberries"))




def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
print(extract_pid("99 elephants in a [cage]"))