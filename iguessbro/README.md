I Guess Bro

![](/iguessbro/screenshoots/1.png)

Diberikan sebuah file chall, yang pas dicek itu adalah file ELF dengan arsitektur RISC-V. Langkah pertamaku adalah melihat strings flag menggunakan `strings chall | grep -i EH4X`, tetapi didapat hanyalah flag palsu. Tanpa ragu-ragu aku pun tanya kepada LLM, intinya di dalam program terdapat pola seperti ini:

```
for (i = 0; i < 35; i++) {
    decoded[i] = encoded[i] ^ (i*7) ^ 0xA5;
}
```

dan ini:

```compare(decoded, input)```


flagnya itu diencoded lalu di-xor, lalu saat runtime baru didecode. Lalu aku minta LLM untuk membuat program untuk mendecode sebagai berikut:

```
python3 - << 'PY'
import struct

path="chall"
data=open(path,"rb").read()

RO_OFF=0x41200
RO_VA =0x51200

start_va=0x57bc8
end_va  =0x57beb

start_off = RO_OFF + (start_va-RO_VA)
end_off   = RO_OFF + (end_va-RO_VA)

enc=data[start_off:end_off]
dec=bytes([(b ^ ((i*7)&0xff) ^ 0xA5) for i,b in enumerate(enc)])
print(dec.decode())
PY
```

Didapat hasil flagnya sebagai berikut

![](/iguessbro/screenshoots/flag.png)
