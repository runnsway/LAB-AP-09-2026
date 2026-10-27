import re
pattern = r'^[A-Z]{1,1}+[a-z]{3,3}+[-]+["X99"|"Y88"|"Z77"]+[0-9]{2,4}+[*+$]{2,2}+$'
daftar_password = [
    "Kzxc-X9912*$",
    "Bqwe-Z771234++",
    "Kzx-X9912*$",
    "kzxc-X9912*$",
    "Kzxc-A1112*$",
    "Bqwe-Z7712345++",
    "Kzxc-X9912*",
    "Kzxc-X9912ab"
]

for i in daftar_password:
    result = re.match(pattern, i)
    if result:
        print("AKSES DITERIMA")
    else:
        print("AKSES DITOLAK")