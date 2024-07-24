# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Rubyscript(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists rubyscript(
        id integer primary key autoincrement,
        rubyrecipe_id text,
            title text,
            script text
    ,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from rubyscript")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from rubyscript where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getallbyrecipeid(self,myid):
        self.cur.execute("select *,'ruby' as mytype from rubyscript where rubyrecipe_id = ?",(myid,))

        job=self.cur.fetchall()
        return job
    def getbyid(self,myid):
        self.cur.execute("select * from rubyscript where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into rubyscript (rubyrecipe_id,title,script) values (:rubyrecipe_id,:title,:script)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["rubyscript_id"]=myid
        azerty["notice"]="votre rubyscript a été ajouté"
        return azerty




