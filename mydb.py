mytable=["country","user","rubyrecipe","pythonrecipe","rubyscript","pythonscript"]
loc={}
for x in mytable:
   exec("from "+x+" import "+x.capitalize(),loc)

class Mydb():
  def __init__(self):
    print("hello")
    for x in mytable:
      loc["self"]=self
      exec("self."+x.capitalize()+"="+x.capitalize()+"()",loc)

