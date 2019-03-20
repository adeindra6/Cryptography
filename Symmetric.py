# Inputkan plaintext yang mau dienkripsi
text = input("Tuliskan Sesuatu : ")

# Inputkan Kunci Caesar
kunci_caesar = input("Kunci Caesar yang diinginkan = ")
try:
    int_kunci_caesar = int(kunci_caesar)
    print("Kunci Caesar anda = " + kunci_caesar)
except ValueError:
    print("Kunci Caesar harus berupa angka")

# Inputkan Kunci Vigenere
kunci_vigenere = input("Kunci Vigenere yang diinginkan = ")
panjang_kunci_vigenere = len(kunci_vigenere)
list_kunci_vigenere = [0 for i in range(panjang_kunci_vigenere)]
try:
    int_kunci_vigenere = int(kunci_vigenere)
    print("Kunci Vigenere anda = " + kunci_vigenere)
    for i in range(panjang_kunci_vigenere):
        list_kunci_vigenere[i] = int(kunci_vigenere[i])
except ValueError:
    print("Kunci Vigenere harus berupa angka")


# Output plaintext yang diinput
print("Plaintext : " + text)
panjang_text = len(text)

# Enkripsi rail fence
railfence_text1 = ""
railfence_text2 = ""
for i in range(panjang_text):
    if i%2 == 0:
        railfence_text1 = railfence_text1 + text[i]
    if i%2 == 1:
        railfence_text2 = railfence_text2 + text[i]

# Output dari hasil enkripsi rail fence
print("Hasil Enkripsi Rail Fence : " + railfence_text1 + railfence_text2)

# Dekripsi rail fence
panjang2_text = len(railfence_text2)
decrypt_text = ""
for i in range(panjang2_text):
    decrypt_text = decrypt_text + railfence_text1[i]
    decrypt_text = decrypt_text + railfence_text2[i]
if panjang_text % 2 == 1:
    decrypt_text = decrypt_text + railfence_text1[panjang2_text]

# Output dari hasil dekripsi rail fence
print("Hasil Dekripsi Rail Fence : " + decrypt_text)

# Enkripsi caesar chiper
caesar_text = ""
for i in range(panjang_text):
    if ord(text[i]) >= 65 and ord(text[i]) <= 90:
        geser = ord(text[i]) + int_kunci_caesar
        while geser > 90:
            geser = geser - 26
        caesar_text = caesar_text + chr(geser)
    elif ord(text[i]) >= 97 and ord(text[i]) <= 122:
        geser = ord(text[i]) + int_kunci_caesar
        while geser > 122:
            geser = geser - 26
        caesar_text = caesar_text + chr(geser)
    elif ord(text[i]) == 32:
        caesar_text = caesar_text + " "

# Output dari hasil enkripsi caesar cipher
print("Hasil Enkripsi Caesar Cipher : " + caesar_text)

# Dekripsi caesar cipher
decrypt_caesar = ""
panjang3_text = len(caesar_text)
for i in range(panjang3_text):
    if ord(caesar_text[i]) >= 65 and ord(caesar_text[i]) <= 90:
        geser = ord(caesar_text[i]) - int_kunci_caesar
        while geser < 65:
            geser = geser + 26
        decrypt_caesar = decrypt_caesar + chr(geser)
    elif ord(caesar_text[i]) >= 97 and ord(caesar_text[i]) <= 122:
        geser = ord(caesar_text[i]) - int_kunci_caesar
        while geser < 97:
            geser = geser + 26
        decrypt_caesar = decrypt_caesar + chr(geser)
    elif ord(text[i]) == 32:
        decrypt_caesar = decrypt_caesar + " "

# Output dari hasil dekripsi caesar cipher
print("Hasil Dekripsi Caesar Cipher : " + decrypt_caesar)

# Enkripsi vigenere cipher
vigenere_text = ""
i = 0
while i < panjang_text:
    for j in range(panjang_kunci_vigenere):
        if ord(text[i]) >= 65 and ord(text[i]) <= 90:
            geser = ord(text[i]) + list_kunci_vigenere[j]
            while geser > 90:
                geser = geser - 26
            vigenere_text = vigenere_text + chr(geser)
        elif ord(text[i]) >= 97 and ord(text[i]) <= 122:
            geser = ord(text[i]) + list_kunci_vigenere[j]
            while geser > 122:
                geser = geser - 26
            vigenere_text = vigenere_text + chr(geser)
        elif ord(text[i]) == 32:
            vigenere_text = vigenere_text + " "
        i = i + 1
        if i == panjang_text:
            break
    j = 0

# Output dari hasil enkripsi vigenere cipher
print("Hasil Enkripsi Vigenere Cipher : " + vigenere_text)

# Dekripsi caesar cipher
decrypt_vigenere = ""
i = 0
panjang4_text = len(vigenere_text)
while i < panjang4_text:
    for j in range(panjang_kunci_vigenere):
        if ord(vigenere_text[i]) >= 65 and ord(vigenere_text[i]) <= 90:
            geser = ord(vigenere_text[i]) - list_kunci_vigenere[j]
            while geser < 65:
                geser = geser + 26
            decrypt_vigenere = decrypt_vigenere + chr(geser)
        elif ord(vigenere_text[i]) >= 97 and ord(vigenere_text[i]) <= 122:
            geser = ord(vigenere_text[i]) - list_kunci_vigenere[j]
            while geser < 97:
                geser = geser + 26
            decrypt_vigenere = decrypt_vigenere + chr(geser)
        elif ord(text[i]) == 32:
            decrypt_vigenere = decrypt_vigenere + " "
        i = i + 1
        if i == panjang4_text:
            break
    j = 0

# Output dari hasil dekripsi vigenere cipher
print("Hasil Dekripsi Vigenere Cipher : " + decrypt_vigenere)