from math import gcd

def find_d(e, m):
    for d in range(1, m):
        if (d * e) % m == 1:
            return d
    return None

def encrypt_rsa(plaintext, e, n):
    return [(ord(char) ** e) % n for char in plaintext]

def decrypt_rsa(ciphertext, d, n):
    return ''.join([chr((char ** d) % n) for char in ciphertext])

nama_lengkap = "Robith saifun nawas"  
p1, q1 = 61, 53  
n1 = p1 * q1
m1 = (p1 - 1) * (q1 - 1)
e1 = 17 
if gcd(e1, m1) != 1:
    raise ValueError("e harus relatif prima terhadap m1")
d1 = find_d(e1, m1)

ciphertext1 = encrypt_rsa(nama_lengkap, e1, n1)
decrypted_name = decrypt_rsa(ciphertext1, d1, n1)

print("Tugas 1: Enkripsi Nama Lengkap")
print("Nama Asli       :", nama_lengkap)
print("Ciphertext      :", ciphertext1)
print("Hasil Dekripsi  :", decrypted_name)

p2, q2 = 3, 7
n2 = p2 * q2
m2 = (p2 - 1) * (q2 - 1)
e2 = 5  
d2 = find_d(e2, m2)

pesan = "HOME"
ciphertext2 = encrypt_rsa(pesan, e2, n2)
decrypted_message = decrypt_rsa(ciphertext2, d2, n2)

print("\nTugas 2: Enkripsi Pesan 'HOME'")
print("Pesan Asli      :", pesan)
print("Ciphertext      :", ciphertext2)
print("Hasil Dekripsi  :", decrypted_message)