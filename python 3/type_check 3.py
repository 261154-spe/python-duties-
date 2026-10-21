# type_check.py
# predictions:
# 8080 is int
# "8080"is str
# "99.51.100.7" is str
# 1_000 is int
print(8080, type(8080))
print("8080", type("8080"))
print(99.5, type(99.5))
print("198.51.100.7", type("198.51.100.7"))
print(1_000, type(1_000))

number = int("443")
text_value = str(8080)
decimal_value = float("2.5")

print(number, type(number))
print(text_value, type(text_value))
print(decimal_value, type(decimal_value))