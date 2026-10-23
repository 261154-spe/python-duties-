# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")

port = int(input("Port: "))

# Error 1: semantic error
is_admin = role == "admin"

# Error 2: syntax error
is_system_port = port <= 1023

# Error 3: semantic error
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
