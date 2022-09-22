"""
Calvin Tian
2022 September 20

Passwords are already in plaintext so there is no decryption or
attack needed. This script simply parses the file and extracts
the passwords to a single text file.
"""

import re

# File locations for input and output files, relative paths
DATABASE_LOCATION = r"Password Lists\yahoo\password.file"
OUTPUT_FULL_LOCATION = r"yahoo_full.txt"
OUTPUT_100_LOCATION = r"submission\yahoo.txt"

# Parse input database
passwords = []
with open(DATABASE_LOCATION, "r") as f:
    PW_RE = r"\d*:.*:(.*)"
    for line in f:
        line = line.strip()
        match_object = re.match(PW_RE, line)
        if match_object:
            passwords.append(match_object.group(1))

# Save all matches to disk
# Every password separated by a newline
with open(OUTPUT_FULL_LOCATION, "w") as f:
    for pw in passwords:
        f.write(f"{pw}\n")

# Passwords in format for assignment submission (100 matches)
with open(OUTPUT_100_LOCATION, "w") as f:
    for i in range(100):
        pw = passwords[i]
        f.write(f"{pw} {pw}\n")

