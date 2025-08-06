import socket
from datetime import datetime

# Dictionary of common ports and their service names
common_ports = {
    20: "FTP (Data)", 21: "FTP (Control)", 22: "SSH", 23: "Telnet",
    25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 3306: "MySQL", 8080: "HTTP-Alt"
}

# Get user input for target IP and port range
target = input("Enter the IP address to scan: ")

try:
    start_port = int(input("Enter starting port number: "))
    end_port = int(input("Enter ending port number: "))

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Please enter values between 1 and 65535.")
        exit()

except ValueError:
    print("Please enter valid numbers for port range.")
    exit()

# Open file to save results
output_file = open("scan_results.txt", "w")
output_file.write(f"Scan results for {target}\n")
output_file.write(f"Port range: {start_port} to {end_port}\n\n")

print(f"\nStarting scan on {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now()

# Scan each port in the specified range
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)  # Set timeout to skip slow responses

    result = sock.connect_ex((target, port))  # Try connecting

    if result == 0:
        service = common_ports.get(port, "Unknown service")
        print(f"Port {port} is OPEN ({service})")
        output_file.write(f"Port {port} is OPEN ({service})\n")

    sock.close()

# End scan and show duration
end_time = datetime.now()
duration = end_time - start_time

print(f"\nScan completed in {duration}")
output_file.write(f"\nScan completed in {duration}\n")
output_file.close()

      
 
