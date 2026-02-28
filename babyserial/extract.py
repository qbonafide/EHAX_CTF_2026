import csv
import base64

input_file = "full.csv"
output_file = "flag.png"

b64_chars = []

with open(input_file, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        v = row["Value"]
        if v and len(v) == 1:
            # hanya ambil karakter base64 valid
            if v in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=":
                b64_chars.append(v)

b64 = "".join(b64_chars)

print("[+] total chars:", len(b64))
print("[+] first 50:", b64[:50])
print("[+] last 50:", b64[-50:])

# fix padding aman
padding = len(b64) % 4
if padding:
    b64 += "=" * (4 - padding)

# decode
decoded = base64.b64decode(b64)

with open(output_file, "wb") as f:
    f.write(decoded)

print("[+] SUCCESS! flag.png created")
