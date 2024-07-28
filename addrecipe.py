from fichier import Fichier
from rubyrecipe import Rubyrecipe
from pythonrecipe import Pythonrecipe
y= tuple(Fichier("./","ruby.txt").lire().split("\n"))
z= tuple(Fichier("./","python.txt").lire().split("\n"))
print(y)
print(z)
for x in y:
    if x != "":
        Rubyrecipe().create({"name":x})
for x in z:
    if x != "":
        Pythonrecipe().create({"name":x})
