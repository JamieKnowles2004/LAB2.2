# Name: Jamie Knowles
# Student Number: C00307559
# Date: 14/10/2025
# Purpose: Find top 5 attacker IPs by failed login attempts and export results to a file.

from collections import defaultdict
import time

def ip_parse(line):
    """Extract an IP address using token-based extraction."""
    parts = line.split()
    for word in parts:
        if word.count('.') == 3:  # simple IP check
            return word
    return None

def main():
    filename = "mixed_logs_5000.log"
    counts = defaultdict(int)

    start = time.time()  # Start timer

    try:
        with open(filename, 'r') as f:
            for line in f:
                if "Failed password" in line or "Invalid user" in line:
                    ip = ip_parse(line)
                    if ip:
                        counts[ip] += 1

        # Sort and get top 5 attacker IPs
        top5 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]

        # Print nicely formatted list
        print("Top 5 attacker IPs:")
        for i, (ip, count) in enumerate(top5, start=1):
            print(f"{i}. {ip} = {count}")

        # Write all counts to a file
        with open("failed_counts.txt", "w") as out_file:
            out_file.write("ip,failed_count\n")
            for ip, count in counts.items():
                out_file.write(f"{ip},{count}\n")

        end = time.time()  # End timer
        print("\nWrote failed_counts.txt")
        print("Elapsed:", round(end - start, 2), "seconds")

    except FileNotFoundError:
        print(f"File '{filename}' not found. Please make sure it exists in the same folder.")

if __name__ == "__main__":
    main()