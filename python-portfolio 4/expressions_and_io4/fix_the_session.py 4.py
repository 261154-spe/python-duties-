
username = input("Username: ")
seconds = int(input("Session length in seconds: "))

minutes = seconds // 60
remaining = seconds % 60

print("=" * 30)
print(f"User: {username}")
print(f"Session: {minutes} min {remaining} s")
print("=" * 30)
