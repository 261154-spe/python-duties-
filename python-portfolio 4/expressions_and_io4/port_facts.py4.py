
PORT_BITS = 16
IPV4_BITS = 32

ports = 2 ** PORT_BITS
highest = ports - 1
addresses = 2 ** IPV4_BITS

print(f"Possible port numbers: {ports}")
print(f"Highest port number: {highest}")
print(f"Possible IPv4 addresses: {addresses}")
