import os
class Fichier:
  def __init__(self,path,name):
    self.path=path
    self.name=name
  def lire(self):
    print(self.path+"/"+self.name)
    j=open(self.path+"/"+self.name, "r")
    return j.read()
  def ligneparligne(self):
    j=open(self.path+"/"+self.name, "r")
    return j.readlines()
  def liretousfichiers(self):
    list=os.listdir(self.path)
    mytext=""
    for yeah in list:
      j=open(self.path+"/"+yeah, "rb")
      mytext+=j.read().decode()
    return mytext.replace("\n","<br>")
  def lirefichier(self):
    print(self.path+"/"+self.name)
    j=open(self.path+"/"+self.name, "rb")
    return j.read()
  def ecrire(self,mycontent):
    hey=open((self.path+"/"+self.name),"w")
    hey.write(mycontent)
    hey.close()
