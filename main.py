import ipaddress
from ping3 import ping

def scan_network(network_range):
    available_devices = []

    try:
        network = ipaddress.IPv4Network(network_range, strict=False)
    except ValueError as e:
        print(f"Invalid network range: {e}")
        return available_devices

    for ip in network:
        try:
            response_time = ping(str(ip), timeout=1)
            if response_time is not None:
                available_devices.append((str(ip), response_time))
        except Exception as e:
            print(f"Ping error: {e}")
        except KeyboardInterrupt:
            print("Scan interrupted.")
            break

    return available_devices

if __name__ == "__main__":
    network_range = input("Enter the network range (e.g., '192.168.1.0/24'): ")
    devices = scan_network(network_range)

    if devices:
        print("Available devices:")
        for ip, response_time in devices:
            print(f"{ip} - Response time: {response_time} ms")
    else:
        print("No available devices found.")
