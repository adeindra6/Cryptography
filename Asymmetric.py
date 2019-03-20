import sympy

# Inputkan plaintext yang mau dienkripsi
text = input("Tuliskan Sesuatu : ")
panjang_text = len(text)

# Inputkan kunci RSA
p = input("Masukkan salah satu angka prima : ")
try:
    int_p = int(p)
    print("p = " + p)
except ValueError:
    print("P harus berupa angka")
q = input("Masukkan salah satu angka prima : ")
try:
    int_q = int(q)
    print("q = " + q)
except ValueError:
    print("q harus berupa angka")

# Enkripsi RSA
rsa_encrypt = ""
if sympy.isprime(int_p) and sympy.isprime(int_q):
    n = int_p * int_q
    z = (int_p-1) * (int_q-1)
    e = int_p
    d = (z+1)/e
    for i in range(panjang_text):
        if text[i].isupper():
            m = pow(ord(text[i]) - 64,e)
            c = m % n
            rsa_encrypt = rsa_encrypt + chr(c + 64)
        elif text[i].islower():
            m = pow(ord(text[i]) - 96, e)
            c = m % n
            rsa_encrypt = rsa_encrypt + chr(c + 96)
else:
    print("Angka tersebut bukan angka prima")

# Output dari hasil enkripsi RSA
print("Hasil Enkripsi RSA : " + rsa_encrypt)

# Dekripsi RSA
panjang2_text = len(rsa_encrypt)
rsa_decrypt = ""
for i in range(panjang2_text):
    if text[i].isupper():
         c = pow(c, int(d))
         m = c % n
         m = m + 64
         rsa_decrypt = rsa_decrypt + chr(m)
    elif text[i].islower():
         c = pow(c, int(d))
         m = c % n
         m = m + 96
         rsa_decrypt = rsa_decrypt + chr(m)

# Output dari hasil dekripsi RSA
print("Hasil Dekripsi RSA : " + rsa_decrypt)