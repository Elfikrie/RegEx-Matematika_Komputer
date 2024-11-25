# Search -> Mencari objek spesifik
import re
teks = "Ada 1 apel, 2 jeruk, dan 3 pisang."

hasil = re.search('jeruk', teks)
if hasil:
  print("Kata 'jeruk' ditemukan!")