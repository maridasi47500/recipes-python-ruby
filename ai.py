# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Ai(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists ai(
        id integer primary key autoincrement,
        username text,
            user_id text,
            mypic text,
            name text,
            description text,
            gender text
    ,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from ai")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from ai where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def findbyuserid(self,myid):
        self.cur.execute("select * from ai where user_id = ?",(myid,))
        azer=self.cur.fetchone()
        row ={"name":"","mypic":"","username":""}
        if azer is not None:
          row=dict(azer)
          print(row["id"], "row id")
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from ai where id = ?",(myid,))
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
          self.cur.execute("insert into ai (username,user_id,mypic,name,description,gender) values (:username,:user_id,:mypic,:name,:description,:gender)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["ai_id"]=myid
        azerty["notice"]="votre ai a été ajouté"
        return azerty




