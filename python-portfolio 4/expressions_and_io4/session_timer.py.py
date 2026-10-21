
seconds = int(input("Enter seconds: "))

minutes = seconds // 60
remaining = seconds % 60

print(f"Session: {minutes} minutes and {remaining} seconds")
    
# Tests:
# 905 = 15 minutes and 5 seconds
# 60 = 1 minute and 0 seconds
# 59 = 0 minutes and 59 seconds