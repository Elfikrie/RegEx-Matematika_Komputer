# [a-zA-Z] -> Mengembalikan karakter apapun yang merupakan lower case danupper case dari a sampai e
import re

text = "Ada 1 apel, 2 jeruk, dan 3 Pisang"
hasil = re.findall('[a-zA-Z]', text)

print(hasil)