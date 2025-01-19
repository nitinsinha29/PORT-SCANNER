# PORT-SCANNER
A  Python script that scans a target IP address or a range of IP addresses for open ports. Open ports indicate services running on the target system, which can be used for various purposes, including system administration, security assessments, and penetration testing.
Core Functionality:

Target Specification:
Allow the user to input the target IP address or a range of IP addresses.
Handle input validation to ensure valid IP addresses are provided.

Port Selection:
Allow the user to specify a range of ports to scan (e.g., 1-1024, 20-25, etc.) or scan all common ports.
Option to provide a list of specific ports to scan.

Scanning Logic:
Utilize Python's socket library to attempt connections to each port on the target(s).
Implement a timeout mechanism to avoid indefinite waits for unresponsive ports.
Log successful connections (open ports) and their corresponding services (if possible).

Output:
Display the results of the scan in a clear and organized manner.
Options to output results to a file (e.g., CSV, text) for later analysis.

Error Handling:
Gracefully handle potential errors, such as invalid IP addresses, network connectivity issues, and unexpected exceptions.
Provide informative error messages to the user.

How To Use :
This Project will only execuete On Linux operating System
save the file on folder with .py extension
execute it on terminal as filename.py
After that write the port , it will scan and tells you about open port
