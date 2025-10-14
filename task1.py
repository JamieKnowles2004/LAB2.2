# Name: Jamie Knowles
# Student Number: C00307559
# Date: 14/10/2025
# Purpose: Read a log file, extract unique IP addresses, and display summary info.

def ip_parse(line):
    """Extract an IP address using token-based extraction."""
    parts = line.split()
    for word in parts:
        if word.count('.') == 3:  # simple check for IP format
            return word
    return None

def main():
    filename = "sample_auth_small.log"
    total_lines = 0
    unique_ips = set()

    try:
        with open(filename, 'r') as file:
            for line in file:
                total_lines += 1
                ip = ip_parse(line)
                if ip:
                    unique_ips.add(ip)

        # Print results
        print(f"Lines read: {total_lines}")
        print(f"Unique IPs: {len(unique_ips)}")
        print("First 10 IPs:", sorted(list(unique_ips))[:10])

    except FileNotFoundError:
        print(f"File '{filename}' not found. Please make sure it exists in the same folder.")

if __name__ == "__main__":
    main()