#2. Penyaringan username
import re

def validasi_username(username):
    pola = r"^[A-Za-z][A-Za-z0-9_]{4,11}$"
    hasil = re.match(pola, username)
    return hasil is not None

def main():
    daftar_valid = []
 
    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.")
    print()

    while True:
        try:
            username = input("Masukkan username: ").strip()

            if not username:
                raise ValueError("Username tidak boleh kosong!")

            if not validasi_username(username):
                raise ValueError("Username tidak valid!")

            if username in daftar_valid:
                raise ValueError("Username sudah terdaftar.")
            
            if username.strip().upper() == "SELESAI":
                break

            print("Username Tersedia.")
            print()
            daftar_valid.append(username)

        except ValueError as e:
            print(f"{e}\n")

    print()
    print("=== Rekapitulasi ===")
    if len(daftar_valid) == 0:
        print("Belum ada username yang valid.")
    else:
        print("Username valid:")
        nomor = 1
        for nama in daftar_valid:
            print(f"{nomor}. {nama}")
            nomor += 1
 
    print()
    print("Jumlah username valid:", len(daftar_valid))
  
main()