from directory import Directory
from render_figure import RenderFigure
from myscript import Myscript
from user import User
from country import Country
from somehtml import Somehtml
from scriptpython import Scriptpython


from mydb import Mydb
from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.dbUsers=User()
        self.Program=Directory("mme AI")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.dbCountry=Country()
        self.db=Mydb()
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
          
    def get_this_route_param(self,myparams={},params=""):
          print("set session",myparams)
          return dict(zip(myparams,params["routeparams"]))
          
    def logout(self,search):
        self.Program.logout()
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def hello(self,search):
        print("hello action")

        if self.Program.get_session()["user_id"] is not None and self.Program.get_session()["user_id"] != "":
          N=3
          ai=self.db.Ai.findbyuserid(self.Program.get_session()["user_id"])
          self.render_figure.set_param("ai",ai)
          theList=self.db.Post.getallaibyid(ai["id"])
          subList = [{"hey":theList[n:n+N]} for n in range(0, len(theList), N)]
          print(subList,"SUBLIST")
          self.render_figure.set_param("subList",subList)
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
    def seeai(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)

        if self.Program.get_session()["user_id"] is not None and self.Program.get_session()["user_id"] != "":
          N=3
          ai=self.db.Ai.findbyuserid(self.Program.get_session()["user_id"])
          self.render_figure.set_param("ai",ai)
          myparam=self.get_this_route_param(getparams,params)
          theList=self.db.Post.getallaibyid(ai["id"])
          subList = [{"hey":theList[n:n+N]} for n in range(0, len(theList), N)]
          self.render_figure.set_param("subList",subList)
        return self.render_figure.render_figure("welcome/myai.html")
    def editpost(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("post",self.db.Post.getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/editpost.html")
    def deletepost(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        x=self.db.Post.deletebyid(myparam["id"])
        
        print("redirect carte didentite")
        self.set_notice("votre post a été supprimé")
        self.set_json("{\"redirect\":\"/\"}")
        return self.render_figure.render_json()
    def showpythonrecipe(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("recipe",self.db.Pythonrecipe.getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/seerecipe.html")
    def showrubyrecipe(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("recipe",self.db.Rubyrecipe.getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/seerecipe.html")
    def showpythonrecipe(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("recipe",self.db.Pythonrecipe.getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/seerecipe.html")
    def showrubyrecipe(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("recipe",self.db.Rubyrecipe.getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/seerecipe.html")
    def seeuser(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        return self.render_figure.set_param("user",User().getbyid(myparam["id"]))
    def update_user(self,params={}):
        myparam=self.post_data(self.getparams)
        self.user=self.dbUsers.update(params)
        self.set_session(self.user)
        self.set_redirect(("/seeuser/"+params["id"][0]))
    def login(self,s):
        search=self.get_post_data()(params=("email","password"))
        self.user=self.dbUsers.getbyemailpwsecurity(search["email"],search["password"])
        print("user trouve", self.user)
        if self.user["email"] != "":
            print("redirect carte didentite")
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/\"}")
        else:
            self.set_json("{\"redirect\":\"/sign_in\"}")
            print("session login",self.Program.get_session())
        return self.render_figure.render_json()
    def nouveau(self,search):
        return self.render_figure.render_figure("welcome/new.html")

    def signup(self,search):
        return self.render_figure.render_figure("user/signup.html")
    def editmyai(self,search):
        return self.render_figure.render_figure("welcome/editmyai.html")
    def newstuff(self,search):
        return self.render_figure.render_figure("welcome/formstuff.html")
    def signin(self,search):
        return self.render_figure.render_figure("user/signin.html")

    def updatepost(self,params={}):
        myparam=self.get_post_data()(params=("id","description",))
        self.user=self.db.Post.update(myparam)
        if self.user["post_id"]:
            self.set_notice("vous avez bien updaté votre post")
            self.set_json("{\"redirect\":\"/posts/"+str(self.user["post_id"])+"\"}")
            return self.render_figure.render_json()
        else:
            self.set_notice("erreur pour updater votre post")
            self.set_json("{\"redirect\":\"/editpost/"+str(self.user["post_id"])+"\"}")
            return self.render_figure.render_json()
    def save_ai(self,params={}):
        myparam=self.get_post_data()(params=("user_id","name","username","mypic","gender","description",))
        self.user=self.db.Ai.update(myparam)
        if self.user["ai_id"]:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
        else:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/editmyai\"}")
            return self.render_figure.render_json()
    def pythonrecipe(self,params={}):
        myparam=self.get_post_data()(params=("myid",))
        script=self.db.Pythonscript.getbyid(myparam["myid"])["script"]
        wow=Scriptpython(script)
        a=wow.lancer1()
        print(script)
        self.set_notice("votre python script a pas été ajouté erreur")
        self.set_json("{\"redirect\":\"/pythonrecipe/"+str(myparam["pythonrecipe_id"])+"\"}")
        return self.render_figure.render_json()
    def rubyrecipe(self,params={}):
        myparam=self.get_post_data()(params=("myid",))
        script=self.db.Rubyscript.getbyid(myparam["myid"])["script"]
        wow=Scriptpython(script)
        a=wow.lancer1()
        print(script)
        self.set_notice("votre ruby script a pas été ajouté erreur")
        self.set_json("{\"redirect\":\"/rubyrecipe/"+str(myparam["rubyrecipe_id"])+"\"}")
        return self.render_figure.render_json()
    def addrubyrecipe(self,params={}):
        myparam=self.get_post_data()(params=("rubyrecipe_id","title","script",))
        self.user=self.db.Rubyscript.create(myparam)
        if self.user["rubyscript_id"]:
            self.set_notice("votr ruby script a été ajouté")
            self.set_json("{\"redirect\":\"/rubyrecipe/"+str(myparam["rubyrecipe_id"])+"\"}")
            return self.render_figure.render_json()
        else:
            self.set_notice("votre ruby script a pas été ajouté erreur")
            self.set_json("{\"redirect\":\"/rubyrecipe/"+str(myparam["rubyrecipe_id"])+"\"}")
            return self.render_figure.render_json()
    def addpythonrecipe(self,params={}):
        myparam=self.get_post_data()(params=("pythonrecipe_id","title","script",))
        self.user=self.db.Pythonscript.create(myparam)
        if self.user["pythonscript_id"]:
            self.set_notice("votr python script a été ajouté")
            self.set_json("{\"redirect\":\"/pythonrecipe/"+str(myparam["pythonrecipe_id"])+"\"}")
            return self.render_figure.render_json()
        else:
            self.set_notice("votr python script a pas été ajouté erreur")
            self.set_json("{\"redirect\":\"/pythonrecipe/"+str(myparam["pythonrecipe_id"])+"\"}")
            return self.render_figure.render_json()
    def save_user(self,params={}):
        myparam=self.get_post_data()(params=("country_id","phone","email","gender","mypic","password","password_security","nomcomplet"))
        self.user=self.dbUsers.create(myparam)
        if self.user["user_id"]:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
        else:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/sign_up\"}")
            return self.render_figure.render_json()
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
            "^/addpythonrecipe$":self.addpythonrecipe,
            "^/addrubyrecipe$":self.addrubyrecipe,
            "^/ruby$":self.rubyrecipe,
            "^/python$":self.pythonrecipe,
            "^/rubyrecipe/([0-9]+)$":self.showrubyrecipe,
            "^/pythonrecipe/([0-9]+)$":self.showpythonrecipe,
            '^/welcome$': self.welcome,
            '^/signin$': self.signin,
            '^/logmeout$':self.logout,
            '^/save_user$':self.save_user,
            '^/update_user$':self.update_user,
            "^/seeuser/([0-9]+)$":self.seeuser,
            "^/edituser/([0-9]+)$":self.edit_user,
            "^/deleteuser/([0-9]+)$":self.delete_user,
            '^/login$':self.login,
            '^/sign_up$':self.signup,
            '^/sign_in$':self.signin,

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
