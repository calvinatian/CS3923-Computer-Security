"""
Calvin Tian
2022 September 14

Using the plaintext passwords from Yahoo, generate SHA-256
hashes with salts from 1000-9999 prepended for every password
and compare to hashes inside the leak. Save the matches.
"""

from collections import defaultdict
import hashlib

# File locations for input and output files, relative paths
INPUT_DATABASE_LOCATION = r"Password Lists\formspring\formspring.txt"
INPUT_PASSWORD_FILE = r"yahoo_full.txt"
OUTPUT_FULL_LOCATION = r"formspring_full.txt"
OUTPUT_100_LOCATION = r"submission\formspring.txt"

# Read all the hashes and store their frequency
hash_count = defaultdict(int)
with open(INPUT_DATABASE_LOCATION, "r") as f:
    for line in f:
        line = line.strip()
        hash_count[line] += 1

# Read all Yahoo plaintext passwords and store their frequency
passwords = defaultdict(int)
with open(INPUT_PASSWORD_FILE, "r") as f:
    for line in f:
        pw = line.strip()
        passwords[pw] += 1

# Generate and compare SHA-256 hashes between Yahoo and Formspring
# Sort by most common Yahoo passwords
decrypted = defaultdict(str)
salt_range = range(1000, 10000)  # Salt range, random guess
for pw, freq in sorted(passwords.items(), key=lambda item: item[1]):
    for salt in salt_range:
        pw_hash = hashlib.sha256(f"{salt}{pw}".encode("utf-8")).hexdigest()
        if pw_hash in hash_count:
            decrypted[pw_hash] = pw
            break
    if len(decrypted) >= 100:  # Stop after 100 matches
        break

# Save all matches to disk
# Every password separated by a newline
with open(OUTPUT_FULL_LOCATION, "w") as f:
    for pw_hash, pw in decrypted.items():
        f.write(f"{pw_hash} {pw}\n")

# Passwords in format for assignment submission (100 matches)
with open(OUTPUT_100_LOCATION, "w") as f:
    for i, (pw_hash, pw) in enumerate(decrypted.items()):
        if i >= 100:
            break
        f.write(f"{pw_hash} {pw}\n")
