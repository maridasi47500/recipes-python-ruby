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
        self.cur.execute("""create table if not exists lignecommandesql(
        id integer primary key autoincrement,
        ligne text
        );""")
        self.con.commit()
        #self.con.close()
    def execute(self,ligne):
        try:
            self.cur.execute(ligne)
            if "select" not in ligne:
                self.con.commit()
            row=self.cur.fetchall()
        except:
            row={}
        return row
