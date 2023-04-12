#!/usr.bin.env python3
"""learning about for logic"""

vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
approved_vendors = ["cisco", "big_ip",  "arista"]

for vendor in approved_vendors:
    print(f"Our vendor is {vendor}.", end="")
    if vendor in approved_vendors:
        print("<= This is an approved vendor!")

print("\nOur loop has ended.")
