
MAX_LOGIN_ATTEMPTS = 5

name = input("Username: ")
failed = int(input("Failed attempts: "))

left = MAX_LOGIN_ATTEMPTS - failed

print("=" * 30)
print("LOGIN REPORT")
print("=" * 30)
print(f"User: {name}")
print(f"Failed: {failed}")
print(f"Attempts left: {left}")

