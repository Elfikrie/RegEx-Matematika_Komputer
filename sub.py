# Sub -> Mengganti suatu karakter
import re
teks = "Ada 1 apel 2 jeruk dan 3 pisang."

hasil = re.sub('[0-9]', '$', teks)
print("sub:", hasil)