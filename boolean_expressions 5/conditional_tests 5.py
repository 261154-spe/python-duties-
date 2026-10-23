#conditional_tests 5

user = "wesam"
role = "viewer"
failed = 3
port = 12

print("Is the failed = 3? I predict True.")
print(failed == 3)
print()
print("Is the port = 123? I predict False.")
print(port == 123)
print()
print("Is the port != 11? I predict True.")
print(port != 11)
print()
print("Is the failed > 2? I predict True.")
print(failed > 2)
print()
print("Is the port >= 10? I predict True.")
print(port >= 10)
print()
print("Is the failed == 2? I predict False.")
print(failed == 2 and port !=12)
print()
print("Is the port ==13? I predict False.")
print(not(port == 13))
print()
print("Is the failed != 3? I predict False.")
print(failed != 3)
print()
print("Is the port <= 15? I predict True.")
print(port <= 15)
print()
print("Is the user admin? I predict False.")
print(user == "admin")