from directory import Directory
from render_figure import RenderFigure
from myscript import Myscript
from user import User
from executeprogram import Executeprogram
from myrecording import Myrecording
from country import Country
from quickstart import Quickstart
from rubyonrailsquickstart import RubyonrailsQuickstart
from vmwarequickstart import VmwareQuickstart
from reversequickstart import ReverseQuickstart
from periode import Periode
from image import Image
from somehtml import Somehtml
from stuff import Stuff
from group_stuff import Group_stuff
from hack import Hack
from lignecommande import Lignecommande
from lignecommandesql import Lignecommandesql


from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.dbUsers=User()
        self.Program=Directory("Hacking avec python")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.dbScript=Myscript()
        self.dbRecording=Myrecording()
        self.Lignecommande=Lignecommande
        self.dbStuff=Stuff()
        self.Quickstart=Quickstart()
        self.RubyonrailsQuickstart=RubyonrailsQuickstart()
        self.VmwareQuickstart=VmwareQuickstart()
        self.ReverseQuickstart=ReverseQuickstart()
        self.dbGroupStuff=Group_stuff()
        self.executeprogram=Executeprogram()
        self.dbPeriode=Periode()
        self.dbImage=Image()
        self.dbCountry=Country()
        self.dbHack=Hack()
        self.render_figure=RenderFigure(self.Program)
        self.getparams=("id",)
    def set_post_data(self,x):
        self.post_data=x
    def get_post_data(self):
        return self.post_data
    def set_my_session(self,x):
        print("set session",x)
        self.Program.set_my_session(x)
        self.render_figure.set_session(self.Program.get_session())
    def set_redirect(self,x):
        self.Program.set_redirect(x)
        self.render_figure.set_redirect(self.Program.get_redirect())
    def render_some_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_some_json(x)
    def render_my_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_my_json(x)
    def set_json(self,x):
        self.Program.set_json(x)
        self.render_figure.set_json(self.Program.get_json())
    def set_notice(self,x):
        print("set session",x)
        self.Program.set_session_params({"notice":x})
        self.render_figure.set_session(self.Program.get_session())
    def set_session(self,x):
          print("set session",x)
          self.Program.set_session(x)
          self.render_figure.set_session(self.Program.get_session())
    def get_this_get_param(self,x,params):
          print("set session",x)
          hey={}
          for a in x:
              hey[a]=params[a][0]
          return hey
          
    def get_this_route_param(self,x,params):
          print("set session",x)
          return dict(zip(x,params["routeparams"]))
          
    def logout(self,search):
        self.Program.logout()
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def envoiemail(self,search):
        return self.render_figure.render_figure("welcome/formemail.html")
    def chat(self,search):
        hi=self.dbScript.getall()
        self.render_figure.set_param("scripts",hi)
        return self.render_figure.render_figure("welcome/chat.html")
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def lancerfauxrouteur(self,search):
        hi=Lignecommande(myscript="lancer le faux routeur")
        hi.ligne(lignecommande="python3 monscript/scriptwlan.py")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def fauxrouteur(self,search):
        hi=Lignecommande(myscript="installer les trucs pour le faux routeur")
        hi.ligne(lignecommande="sh monscript/fauxrouteur.sh")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def fileserver2(self,search):
        hi=Lignecommande(myscript="modifier le port et l'hôte")
        hi.ligne(lignecommande="sh monscript/monserverfichier.sh")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def fileserver3(self,search):
        hi=Lignecommande(myscript="demarrer le serveur de fichier ")
        hi.ligne(lignecommande="sudo fileserver/install")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def fileserver4(self,search):
        hi=Lignecommande(myscript="demarrer le serveur de fichier ")
        hi.ligne(lignecommande="sudo fileserver/uninstall")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def fileserver1(self,search):
        hi=Lignecommande(myscript="lire à propos de serveur de fichier")
        hi.ligne(lignecommande="cat fileserver/README.md")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def fausseimprimante3(self,search):
        hi=Lignecommande(myscript="lire à propos de la fausse imprimante")
        hi.ligne(lignecommande="cat IPPSERVERREADME.md")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def fausseimprimante2(self,search):
        hi=Lignecommande(myscript="lancer la fausse imprimante2")
        hi.ligne(lignecommande="python -m ippserver --port 1234 save /tmp/")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def fausseimprimante1(self,search):
        hi=Lignecommande(myscript="fausse imprimante script 1")
        hi.ligne(lignecommande="sudo python3 printer1.py install")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def executemysql(self,search):
        aze=self.get_post_data()(params=("lignecommande",))
        self.Program.set_session_params({"mysql":aze["lignecommande"]})
        x=Lignecommandesql().execute(aze["lignecommande"])
        self.render_figure.set_param("redirect","/mysql")
        return self.render_some_json("welcome/redirect.json")
    def lancerserveuremail(self,search):
        aze=self.get_post_data()(params=("from","to","content","password","object",))
        hi=Lignecommande(myscript="lancer le serveur demail")
        hi.ligne(lignecommande="sudo fakesmtpd --mail-dir=mail_dir --log-file=logemail.log --host='127.0.0.1' --port=587")
        hi.run()
        self.set_notice("ok pour le script")
        return self.render_some_json("welcome/emailimprim.json")
    def createemail(self,search):
        aze=self.get_post_data()(params=("from","to","content","password","object",))
        email=self.Lignecommande("MONSCRIPT : BIENVENUE : envoi de lemail")
        lignecommande = "from='{sender_email}' to='{receiver_email}' content='{content}' object='{object}' python3 envoidemail.py".format(sender_email=aze["from"], receiver_email=aze["to"],port=587,smtp_server="127.0.0.1",content=aze["content"],object=aze["object"]).replace("'","\'")
        print(lignecommande)
        email.ligne(lignecommande = lignecommande)
        msg=email.run()
        self.set_notice("une fenetre a lance le program")
        return self.render_some_json("welcome/emailimprim.json")
    def allscript(self,search):
        #myparam=self.get_post_data()(params=("name","content",))
        hi=self.dbScript.getall()
        self.render_figure.set_param("scripts",hi)
        return self.render_figure.render_figure("welcome/allscript.html")
    def lancerscript(self,search):
        myparam=search["myid"][0]
        hi=self.dbScript.getbyid(myparam)
        print(hi, "my script")
        a=self.scriptpython(hi["name"]).lancer()
        return self.render_some_json("welcome/monscript.json")


    def new1(self,search):
        myparam=self.get_post_data()(params=("script","missiontarget_id","missiontype_id","missionprogram_id",))
        #hi=self.dbMissionscript.create(myparam)
        return self.render_some_json("welcome/mypic.json")
    def nouvelleimage(self,search):
        myparam=self.get_post_data()(params=("text","pic","mf"))
        self.render_figure.set_param("redirect","/")
        x=self.dbImage.create(myparam)
        if x["image_id"]:
          self.set_notice("votre image a été ajoutée")
        else:
          self.Program.set_code422(True)
          self.set_notice("erreur quand votre image a été ajoutée")
        return self.render_some_json("welcome/redirect.json")
    def monscript(self,search):
        myparam=self.get_post_data()(params=("name","content",))
        hey=self.dbCommandline.create(myparam)
        hi=self.dbScript.create(myparam)
        print(hey,hi)
        return self.render_some_json("welcome/monscript.json")
    def enregistrer(self,search):
        print("hello action")
        self.render_figure.set_param("enregistrer",True)
        return self.render_figure.render_figure("welcome/radio.html")
    def emailimprim(self,search):
        print("hello action")
        return self.render_figure.render_figure("welcome/emailimprim.html")
    def hakingprojet(self,search):
        print("hello action")
        return self.render_figure.render_figure("welcome/hakingprojet.html")
    def hello(self,search):
        print("hello action")
        self.render_figure.set_param("quickstart",self.Quickstart.getall())
        self.render_figure.set_param("rubyonrailsquickstart",self.RubyonrailsQuickstart.getall())
        self.render_figure.set_param("vmwarequickstart",self.VmwareQuickstart.getall())
        self.render_figure.set_param("reversequickstart",self.ReverseQuickstart.getall())
        return self.render_figure.render_figure("welcome/index.html")
    def delete_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(self.getparams)
        self.render_figure.set_param("user",User().deletebyid(myparam["id"]))
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def edit_user(self,params={}):
        getparams=("id",)

        myparam=self.get_this_route_param(getparams,params)
        print("route params")
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("user/edituser.html")
    def voirlieu(self,params={}):
        getparams=("id",)

        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)

        try:
          lieu1=self.dbLieu.getbyid(myparam["id"])
          self.render_figure.set_param("lieu",self.dbLieu.getbyid(myparam["id"]))
          if not lieu1:
            self.Program.set_code422(True);
            return self.render_some_json("ajouter/lieu1.json")
          return self.render_some_json("ajouter/lieu.json")
        except:
          self.Program.set_code422(True);
          return self.render_some_json("ajouter/lieu1.json")
    def voirpersonne(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        #personn1=self.dbPersonne.getbyid(myparam["id"])
        #self.render_figure.set_param("person",personn1)
        self.render_figure.set_param("event",self.dbEvent.getallbypersonid(personn1["id"]))
        return self.render_figure.render_figure("ajouter/voirpersonne.html")
    def seeuser(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        return self.render_figure.set_param("user",User().getbyid(myparam["id"]))
    def myusers(self,params={}):
        self.render_figure.set_param("users",User().getall())
        return self.render_figure.render_figure("user/users.html")
    def mypics(self,params={}):
        self.render_figure.set_param("pics",self.dbFish.getall())
        return self.render_figure.render_figure("fish/fishes.html")
    def update_user(self,params={}):
        myparam=self.post_data(self.getparams)
        self.user=self.dbUsers.update(params)
        self.set_session(self.user)
        self.set_redirect(("/seeuser/"+params["id"][0]))
    def login(self,s):
        search=self.get_post_data()(params=("email","password","password_security"))
        self.user=self.dbUsers.getbyemailpwsecurity(search["email"],search["password"],search["password_security"])
        print("user trouve", self.user)
        if self.user["email"] != "":
            print("redirect carte didentite")
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/cartedidentite\"}")
        else:
            self.set_json("{\"redirect\":\"/youbank\"}")
            print("session login",self.Program.get_session())
        return self.render_figure.render_json()
    def ajouterimage(self,search):
        return self.render_figure.render_figure("ajouter/image.html")
    def nouveau(self,search):
        return self.render_figure.render_figure("welcome/new.html")
    def getlyrics(self,params={}):
        getparams=("id",)

       
        myparam=self.get_this_get_param(getparams,params)
        print("my param :",myparam)
        try:
          print("hey",hey)
          if not hey:
            hey=[]
        except:
          hey=[]

        self.render_figure.set_param("lyrics",hey)
        return self.render_some_json("welcome/lyrics.json")
    def reseau(self,search):
        return self.render_figure.render_figure("welcome/reseau.html")
    def supprimerlabdd(self,search):
        self.executeprogram.execute("rm somesql.db")
        self.set_json("{\"redirect\":\"/\"}")
        return self.render_figure.render_json()
    def registreedition(self,search):
        self.executeprogram.execute("registre.sh")
        return self.render_figure.render_figure("welcome/hey.html")
    def reversequickstart(self,search):
        myparam=self.get_post_data()(params=("url",))
        wow=self.ReverseQuickstart.create(myparam)
        if wow["reverse_quickstart_id"]:
            self.set_session(wow)
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
        else:
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
    def mysql(self,search):
        print("====================+>mysqlresult",Lignecommandesql().get(self.Program.get_session()["mysql"]))
        self.render_figure.set_param("mysqlresult",Lignecommandesql().get(self.Program.get_session()["mysql"]))

        return self.render_figure.render_figure("welcome/mysql.html")
    #exeutc my sql commande or svae my sql commande to db
    #def executemysql(self,search):
    #    myparam=self.get_post_data()(params=("lignecommande",))
    #    wow=self.Lignecommandesql.create(myparam["lignecommande"])
    #    if wow["lignecommande"]:
    #        self.set_session(wow)
    #        self.set_json("{\"redirect\":\"/mysql\"}")
    #        return self.render_figure.render_json()
    #    else:
    #        self.set_json("{\"redirect\":\"/mysql\"}")
    #        return self.render_figure.render_json()
    def reverse(self,search):
        return self.render_figure.render_figure("welcome/reverse.html")
    def vmwarequickstart(self,search):
        myparam=self.get_post_data()(params=("url",))
        wow=self.VmwareQuickstart.create(myparam)
        if wow["vmware_quickstart_id"]:
            self.set_session(wow)
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
        else:
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
    def vmware(self,search):
        return self.render_figure.render_figure("welcome/vmware.html")
    def rubyonrailsquickstart(self,search):
        myparam=self.get_post_data()(params=("url",))
        wow=self.RubyonrailsQuickstart.create(myparam)
        if wow["rubyonrails_quickstart_id"]:
            self.set_session(wow)
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
        else:
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
    def rubyonrails(self,search):
        return self.render_figure.render_figure("welcome/rubyonrails.html")
    def wiresharkquickstart(self,search):
        myparam=self.get_post_data()(params=("url",))
        wow=self.Quickstart.create(myparam)
        if wow["quickstart_id"]:
            self.set_session(wow)
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
        else:
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
    def wireshark(self,search):
        return self.render_figure.render_figure("welcome/wireshark.html")
    def lignecommandewindows(self,search):
        self.executeprogram.execute("cmd.sh")
        return self.render_figure.render_figure("welcome/hey.html")
    def jouerjeux(self,search):
        return self.render_figure.render_figure("welcome/jeu.html")

    def signin(self,search):
        return self.render_figure.render_figure("user/signin.html")

    def save_user(self,params={}):
        myparam=self.get_post_data()(params=("email","password","password_security","nomcomplet"))
        self.user=self.dbUsers.create(myparam)
        if self.user["user_id"]:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/youbank\"}")
            return self.render_figure.render_json()
        else:
            self.set_json("{\"redirect\":\"/youbank_inscription\"}")
            return self.render_figure.render_json()
    def joueraujeu(self,params={}):
        self.set_json("{\"redirect\":\"/signin\"}")
        getparams=("song_id","jeu_id")
        myparam=self.get_post_data()(params=getparams)
        self.set_session_params(myparam)
        #self.set_redirect("/signin")
        #return self.render_figure.render_redirect()
        return self.render_figure.render_my_json("{\"redirect\":\"/signin\"}")
    def run(self,redirect=False,redirect_path=False,path=False,session=False,params={},url=False,post_data=False):
        if post_data:
            print("post data")
            self.set_post_data(post_data)
            print("post data set",post_data)
        if url:
            print("url : ",url)
            self.Program.set_url(url)
        self.set_my_session(session)

        if redirect:
            self.redirect=redirect
        if redirect_path:
            self.redirect_path=redirect
        if not self.render_figure.partie_de_mes_mots(balise="section",text=self.Program.get_title()):
            self.render_figure.ajouter_a_mes_mots(balise="section",text=self.Program.get_title())
        if path and path.endswith("png"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("html"):
            self.Program=Somehtml(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpeg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("gif"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("svg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith(".jfif"):
            self.Program=Pic(path)
        elif path and path.endswith(".css"):
            self.Program=Css(path)
        elif path and path.endswith(".js"):
            self.Program=Js(path)
        elif path:
            path=path.split("?")[0]
            print("link route ",path)
            ROUTES={
                    '^/supprimerlabdd$': self.supprimerlabdd,
                    '^/fileserver1$': self.fileserver1,
                    '^/fileserver2$': self.fileserver2,
                    '^/fileserver3$': self.fileserver3,
                    '^/fileserver4$': self.fileserver4,
                    '^/fausseimprimante3$': self.fausseimprimante3,
                    '^/fausseimprimante2$': self.fausseimprimante2,
                    '^/fausseimprimante1$': self.fausseimprimante1,
                    '^/lancerserveuremail$': self.lancerserveuremail,
                    '^/imprimemail$': self.emailimprim,
                    '^/createemail$': self.createemail,
                    '^/envoiemail$': self.envoiemail,
                    '^/fauxrouteur$': self.fauxrouteur,
                    '^/lancerfauxrouteur$': self.lancerfauxrouteur,
                    '^/hakingprojet$': self.hakingprojet,
            '^/registreedition$': self.registreedition,
            '^/reseau$': self.reseau,
            '^/lignecommandewindows$': self.lignecommandewindows,
            '^/rubyonrailsquickstart$': self.rubyonrailsquickstart,
            '^/virtualisation$': self.vmware,
            '^/reversequickstart$': self.reversequickstart,
            '^/mysql$': self.mysql,
            '^/executemysql$': self.executemysql,
            '^/reverse$': self.reverse,
            '^/vmwarequickstart$': self.vmwarequickstart,
            '^/script$': self.rubyonrails,
            '^/wiresharkquickstart$': self.wiresharkquickstart,
            '^/wireshark$': self.wireshark,
            '^/nouvelleimage$': self.nouvelleimage,
            '^/ajouterimage$': self.ajouterimage,
            '^/new$': self.nouveau,
            '^/welcome$': self.welcome,
            '^/signin$': self.signin,
            '^/logmeout$':self.logout,
            '^/save_user$':self.save_user,
            '^/update_user$':self.update_user,
            "^/seeuser/([0-9]+)$":self.seeuser,
            "^/edituser/([0-9]+)$":self.edit_user,
            "^/deleteuser/([0-9]+)$":self.delete_user,
            '^/login$':self.login,

                                                                                                    '^/users$':self.myusers,
                    '^/$': self.hello

                    }
            REDIRECT={"/save_user": "/welcome"}
            for route in ROUTES:
               print("pattern=",route)
               mycase=ROUTES[route]
               x=(re.match(route,path))
               print(True if x else False)
               #code bon pour les erreurs dans le code python
               if x:
                   params["routeparams"]=x.groups()
                   try:
                       html=mycase(params)
                   except Exception as e:
                       print("erreur"+str(e),traceback.format_exc())
                       html=("<p>une erreur s'est produite dans le code server  "+(traceback.format_exc())+"</p><a href=\"/\">retour à l'accueil</a>").encode("utf-8")
                       print(html)
                   self.Program.set_html(html=html)
                   self.Program.clear_notice()
                   #self.Program.redirect_if_not_logged_in()
                   return self.Program
               else:
                   self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")

        return self.Program
