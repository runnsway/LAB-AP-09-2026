#1. Validasi Data Mahasiswa
import re

def validasi_nim(nim):
    pola = r"^H071[0-9]{6,6}$"
    hasil = re.match(pola, nim)
    return hasil is not None

def validasi_email(email):
    pola = r"^[A-Za-z0-9._]+@([A-Za-z0-9]+\.)+[A-Za-z]+$"
    hasil = re.match(pola, email)
    return hasil is not None

def validasi_telepon(telepon):
    pola = r"^[0-9]{10,13}$"
    hasil = re.match(pola, telepon)
    return hasil is not None

def main():
    print("=== Validasi Data Mahasiswa ===")
    print()

    nim_valid = False
    email_valid = False
    telepon_valid = False

    while True:
        if not nim_valid:
            nim = input("Masukkan NIM      : ").strip()
            if not nim:
                print("NIM tidak boleh kosong!")
                continue
            elif not validasi_nim(nim):
                print("Format NIM tidak Valid!")
                continue
            nim_valid = True

        if not email_valid:
            email = input("Masukkan Email    : ").strip()
            if not email:
                print("Email tidak boleh kosong!")
                continue
            elif not  validasi_email(email):
                print("Format Email tidak Valid!")
                continue
            email_valid = True

        if not telepon_valid:
            telepon = input("Masukkan No. Telp : ").strip()
            if not telepon:
                print("Nomor telepon tidak boleh kosong!")
                continue
            elif not validasi_telepon(telepon):
                print("Format nomor telepon salah!")
                continue
            telepon_valid = True

        
        break

    print()
    print("--- Hasil Validasi Akhir ---")
    print("NIM         : Valid")
    print("Email       : Valid")
    print("No. Telepon : Valid")
    print("\nData mahasiswa berhasil diverifikasi!")

main()