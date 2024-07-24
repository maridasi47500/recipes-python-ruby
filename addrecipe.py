from fichier import Fichier
from rubyrecipe import Rubyrecipe
from pythonrecipe import Pythonrecipe
for x in Fichier("./","ruby.txt").lire().split("\n"):
  Rubyrecipe().create({"name":x}
for x in Fichier("./","python.txt").lire().split("\n"):
  Pythonrecipe().create({"name":x}
  
