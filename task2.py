# Name: Jamie Knowles
# Student Number: C00307559
# Date: 14/10/2025
# Purpose: Count failed login attempts per IP address from a log file.

from collections import defaultdict

def ip_parse(line):
    """Extract an IP address using token-based extraction."""
    parts = line.split()
    for word in parts:
        if word.count('.') == 3:  # simple IP check
            return word
    return None

def main():
    filename = "sample_auth_small.log"
    counts = defaultdict(int)

    try:
        with open(filename, 'r') as f:
            for line in f:
                # Only count failed logins
                if "Failed password" in line or "Invalid user" in line:
                    ip = ip_parse(line)
                    if ip:
                        counts[ip] += 1

        # Print results
        print("Failed login attempts per IP:")
        for ip, count in counts.items():
            print(f"{ip} : {count}")

    except FileNotFoundError:
        print(f"File '{filename}' not found. Please make sure it exists in the same folder.")

if __name__ == "__main__":
    main()