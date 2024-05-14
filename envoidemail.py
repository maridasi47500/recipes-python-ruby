import smtplib
from email.message import EmailMessage
from os import environ as aze
import traceback
import ssl




class Envoidemail():

  def __init__(self,port=465,smtp_server= "smtp.gmail.com",sender_email = "my@gmail.com",receiver_email = "your@gmail.com",password = "",object = "Hi there", content="This message is sent from Python."):
    fromaddr = sender_email
    toaddrs  = receiver_email
    self.receiver_email  = receiver_email
    self.SMTPServer = smtp_server
    self.port = port #465 #587
    self.login = sender_email
    self.sender_email = sender_email
    self.password = password
    self.message="""Subject: """+object+"""
    """+content+"""
    """
    
    self.msg = EmailMessage()
    msgtxt = content
    self.msg.set_content(msgtxt)
    self.msg['Subject'] = object
    self.msg['From'] = sender_email
    self.msg['To'] = receiver_email
  def envoyer(self):
    try:
      print(self.SMTPServer, self.port)
      ##server=smtplib.SMTP(self.SMTPServer, self.port)
      #server = smtplib.SMTP_SSL(self.SMTPServer, self.port) #use smtplib.SMTP() if port is 587
      #server.set_debuglevel(True)
      ##server.starttls()

      ##server.login(self.login, self.password)

      #server.connect()

      context = ssl.create_default_context()
      server=smtplib.SMTP(self.SMTPServer, self.port)
      server.ehlo()  # Can be omitted
      print("hello")
      #server.starttls(context=context)
      #server.ehlo()  # Can be omitted
      #server.login(self.sender_email, self.password)
      print(self.message)
      print(self.sender_email, self.receiver_email, self.message)
      server.sendmail(self.sender_email, self.receiver_email, self.message)
      server.quit()



      #try:
      #  server.send_message(self.msg)
      #finally:
      #  server.quit()
      return "l'envoi d'email s'est bien passé"
    except Exception as e:
      return str(traceback.format_exc())


email=Envoidemail(sender_email=aze["from"], receiver_email=aze["to"],port=587,smtp_server="127.0.0.1",content=aze["content"],object=aze["object"])
msg=email.envoyer()
print(msg)
