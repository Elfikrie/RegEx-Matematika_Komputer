import re

# teks = "Ada 1 apel 2 Jeruk, dan 3 pisang"

# hasil = re.findall("['a-j']", teks)
# print("findall:", hasil)

# teks = "Ada 1 apel, 2 jeruk, dan 3 pisang"

# hasil = re.findall("['^apel']", teks)
# print("findall:", hasil)

txt = "Abi Baru Cuci Baju di jam 15.38"

# Periksa apakah stringnya memiiki angka 2 digit dari 00 - 59
x = re.findall("[0-5][0-9]", txt)
y = re.findall("[0-100]", txt)

print(x, y)