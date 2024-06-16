# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from chaine import Chaine
import requests
class Lignecommandesql(Model):
    def __init__(self):
        self.con=sqlite3.connect("somesql.db")
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        #self.cur.execute("""create table if not exists lignecommandesql(
        #id integer primary key autoincrement,
        #ligne text
        #);""")
        #self.con.commit()
        #self.con.close()
    def get(self,ligne):
        try:

            if "select" in ligne:
              self.cur.execute(ligne)
              row=self.cur.fetchall()
            else:
              self.cur.execute(ligne)
              row=[{"execute":"ce n'est pas un select c'est insert update ou delete"}]
        except Exception as e:
            print(e)
            row=[{"error":str(e)}]
        self.con.close()
        return row
    def execute(self,ligne):
        try:

            if "select" not in ligne:
              self.cur.execute(ligne)
              self.con.commit()
              row=self.cur.fetchall()
            else:
              self.cur.execute(ligne)
              row=self.cur.fetchall()
        except Exception as e:
            print(e)
            row=[{"error":str(e)}]
        self.con.close()
        return row
