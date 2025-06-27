import numpy as np

def huruf_ke_angka(pesan):
    return [(ord(c.lower()) - 96 if c.isalpha() else 27) for c in pesan]

def angka_ke_huruf(angka):
    return ''.join([chr(num + 96) if 1 <= num <= 26 else ' ' for num in angka])

def get_default_matrix(n):
    np.random.seed(n)  
    while True:
        m = np.random.randint(1, 10, size=(n, n))
        if np.linalg.det(m) != 0:
            return m

def tampilkan_operasi_matriks(matrix, vector, result, operasi="Matriks x Blok"):
    n = len(vector)
    print("    Langkah perkalian:")
    for i in range(n):
        rumus = " + ".join([f"{matrix[i][j]}*{vector[j][0]}" for j in range(n)])
        hasil = " + ".join([str(matrix[i][j]*vector[j][0]) for j in range(n)])
        print(f"      Baris {i+1}: {rumus} = {hasil} = {int(result[i][0])}")

def encode(pesan, matriks):
    n = matriks.shape[0]
    angka = huruf_ke_angka(pesan)

    while len(angka) % n != 0:
        angka.append(27)

    print("\n")
    print("="*56)
    print(f"Hasil konversi huruf ke angka:")
    print("  ", angka)
    print("="*56)
    angka_blok = [angka[i:i+n] for i in range(0, len(angka), n)]

    hasil = []
    print("\n")
    print("="*56)
    print("Langkah-langkah ENCODING:")
    print("="*56)
    for i, blok in enumerate(angka_blok):
        print(f"  Blok {i+1}: {blok}")
        vektor = np.array(blok).reshape((n, 1))
        encoded = np.dot(matriks, vektor)
        tampilkan_operasi_matriks(matriks, vektor, encoded)
        hasil.extend(encoded.flatten().astype(int).tolist())

    return hasil

def decode(encoded_data, matriks):
    n = matriks.shape[0]
    inv = np.linalg.inv(matriks)
    angka_blok = [encoded_data[i:i+n] for i in range(0, len(encoded_data), n)]
    hasil = []
    print("\n")
    print("="*56)
    print("Langkah-langkah DECODING:")
    print("="*56)
    for i, blok in enumerate(angka_blok):
        print(f"  Blok {i+1}: {blok}")
        vektor = np.array(blok).reshape((n, 1))
        decoded = np.dot(inv, vektor)
        rounded = np.round(decoded.flatten()).astype(int)
        tampilkan_operasi_matriks(inv, vektor, decoded, operasi="Invers x Blok")
        hasil.extend(rounded.tolist())

    return hasil

print("="*56)
print("=== ENKRIPSI & DEKRIPSI PESAN DENGAN MATRIX ENCODING ===")
print("="*56)
print("\n")
print("="*56)
pesan = input("masukkan pesan yang ingin diencode: ")
print("="*56)
print("\n")
try:
    print("="*56)
    ukuran = int(input("pilih ukuran nxn matriks encoding (2–10): "))
    print("="*56)
    print("\n")
    if ukuran < 2 or ukuran > 10:
        raise ValueError("Ukuran matriks harus antara 2 dan 10.")
        
    kunci_matriks = get_default_matrix(ukuran)
    print("="*56)
    print(f"matriks encoding {ukuran}x{ukuran} yang digunakan:")
    print(kunci_matriks)
    print("="*56)

    hasil_encode = encode(pesan, kunci_matriks)
    print("="*100)
    print(f"hasil encoding akhir: {hasil_encode}")
    print("="*100)

    hasil_decode = decode(hasil_encode, kunci_matriks)
    pesan_akhir = angka_ke_huruf(hasil_decode)

    print("="*56)
    print(f"pesan hasil decoding: {pesan_akhir}")
    print("="*56)

except ValueError as e:
    print(f"Error: {e}")
