# [a-e] -> Mengembalikan karakter apapun yang merupakan lower case dari a-e
# [A-E] -> Mengembalikan karakter apapun yang merupakan upper case dari a sampai e
import re

text = "Ada 1 apel, 2 jeruk, dan 3 Pisang"
hasil1 = re.findall('[A-Z]', text)
hasil2 = re.findall('[a-z]',text)


print("hasil1:", hasil1)
print("Hasil2: ", hasil2)

