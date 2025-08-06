import socket
from datetime import datetime

# Defining the most common ports
common_ports = {
    20: "FTP (Data)", 21: "FTP (Control)", 22: "SSH", 23: "Telnet",
    25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 3306: "MySQL", 8080: "HTTP-Alt"
}

# Asking user for the IP address
target = input("Enter the IP address to scan: ")

# Asking user for the port range
start_port = int(input("Enter starting port number: "))
end_port = int(input("Enter ending port number: "))
output_file = open("scan_results.txt", "w")

# Writes the information into the file
output_file.write(f"Scan results for {target}\n")
output_file.write(f"Port range: {start_port} to {end_port}\n\n")
print(f"\nStarting scan on {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now() # start time of the scanning

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)  # If host doesn't respond in 0.5 seconds, skip

    result = sock.connect_ex((target, port))

    if result == 0:
        service = common_ports.get(port, "Unknown service")
        print(f"Port {port} is OPEN ({service})")
        output_file.write(f"Port {port} is OPEN ({service})\n")

    sock.close()
    
end_time = datetime.now()
duration = end_time - start_time

print(f"\nScan completed in {duration}")
output_file.write(f"\nScan completed in {duration}\n")
output_file.close()


      
 
