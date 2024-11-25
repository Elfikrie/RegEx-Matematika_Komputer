# [^abc] -> Mengembalikkan karakter apapun selain a, b, dan c
import re

teks = "Ada 1 apel, 2 jeruk, dan 3 pisang"
hasil = re.findall('[^apel]', teks)

print("Hasil:", hasil)

# Jika ingin  kata apelnya saja yang dikecualikan

# \b: Mencocokkan batas kata.
# (?!apel): Grup negatif yang memastikan kata setelahnya bukan "apel".
# \w+: Mencocokkan kata (huruf, angka, dan underscore).
hasil2 = re.findall(r'\b(?!apel)\w+\b', teks)

print("Hasil2:", hasil2)