# device_cerd.py
# This program prints a network device record.
MAX_CONNECTIONS = 100
device_name = "wed_server_01"
device_ip = "192.0.2.20"
service = "HTTPS"
open_port = 443
print("Device:",device_name)
print("IP address:",device_ip)
print("Service:",service)
print("port:",open_port)
print("max connctions:",MAX_CONNECTIONS)

service = "SSH"
open_port = 22

print("Updated service:",service,"on port",open_port)
