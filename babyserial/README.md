Baby Serial

Diberikan chall seperti ini

![](/babyserial/screenshots/1.png)


Dikasih file dengan tipe extention .sal, dari hasil researchku, sal adalah file capture dari Saleae Logic Analyzer, dan file sal ini bisa dianalisis pake tools Logic 2 dari `salae.com`. Aku jalanin toolsnya dari command line menggunakan `./Logic-2.4.14-linux-x64.AppImage --no-sandbox` lalu buka file sal tadi. Terus pilih add analyzer > async serial > masukkan channel: 0 dan baudrate: 115200. Hasilnya, di sebelah kanan itu keliatan strings ascii dalam base64, yang mana merupakan header dari file png.

![](/babyserial/screenshots/2.png)


Terus export aja jadi file csv gitu lalu minta LLM bikin program python buat bersihin dan decode hasil csv dan rewrite ke file png.

![](/babyserial/screenshots/3.png)


```python
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
```

Buka file png terus dapet flag deh


![](/babyserial/screenshots/flag.png)

