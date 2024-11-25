# Findall -> Mencari semua kecocokan dalam suatu list

import re
teks = "Ada 1 apel, 2 jeruk, dan 3 pisang."

hasil = re. findall('[0-9]', teks)
print("Findall:", hasil)