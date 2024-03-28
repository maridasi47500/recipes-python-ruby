from subprocess import check_output as runmyscript
from threading import Thread
import os
from subprocess import Popen, PIPE, STDOUT
try:
    from subprocess import DEVNULL # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')
import subprocess
FNULL = open(os.devnull, 'w')
from subprocess import call
class Executeprogram:
  def __init__(self,hey=""):
    self.hey="./monscript/"+hey
    if hey.endswith(".sh"):
      self.someargs=["sh",self.hey]
    elif hey.endswith(".py"):
      self.someargs=["python3",self.hey]
    elif hey.endswith(".rb"):
      self.someargs=["ruby",self.hey]
    else:
      self.someargs=["python3",self.hey]
    self.runprogram=runmyscript
  def execute(self,hey=""):
    Thread(target=self.executeme, args=(hey,)).start()
  def executeme(self,hey=""):
    self.hey="./monscript/"+hey
    if hey.endswith(".sh"):
      self.someargs=["sh",self.hey]
    elif hey.endswith(".py"):
      self.someargs=["python3",self.hey]
    elif hey.endswith(".rb"):
      self.someargs=["ruby",self.hey]
    else:
      self.someargs=["python3",self.hey]
    text="hey"
    #p = Popen(self.someargs, stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)
    #p.communicate(text.encode('utf-8'))
    #assert p.returncode == 0 # use appropriate for your program error handling here
    runmyscript(self.someargs,stderr=subprocess.STDOUT)
    #call(self.someargs,stdout=FNULL,stderr=subprocess.STDOUT)
  def myargs(self,a):
    #print(a)
    for x in a:
        print("arg len",len(x))
    self.someargs=a
  def run(self):
    return runmyscript(self.someargs).decode()
    
