# -*- coding: utf-8 -*-
from fichier import Fichier

import sys
import os
print(sys.argv[1])


filename=sys.argv[1].lower()
myclass=(filename).capitalize()
modelname=(filename).capitalize()
marouteget="\"/%s\"" % filename
maroutenew="\"/%s_new\"" % filename
maroutecreate="\"/%s_create\"" % filename
marouteget2="\\\"/%s\\\"" % filename
myhtml="my"+filename+"html"
myfavdirectory=filename
form="<form action=\"create"+filename+"\" method=\""+filename+"\">"
index = 2 
createtable=""
columns="("
values="("
myparam=","
items=sys.argv
while index < (len(items)):

    try:
      print(index, items[index])
      paramname=items[index]
      print(items[(index+1)])
    except:
      myparam=""
    index += 1
    form+=""" <div class="field">
<label  for="{filename}_{paramname}">{paramname}</label><input id="{filename}_{paramname}" name="{paramname}" type="text"/></div>
    """.format(filename=filename,paramname=paramname)
columns+=")"
values+=")"

#os.system("mkdir %s" % myfavdirectory)
#pathhtml="%s/%s.html" % (myfavdirectory, myhtml)
#os.system("touch %s" % pathhtml)
form+=""" <div class="actions">
<input id="{filename}_submit" name="submit" value="create {filename}" type="submit"/></div>
    """.format(filename=filename,paramname=paramname)

Fichier("./welcome","form"+filename+".html").ecrire(form)
