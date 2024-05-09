import smtplib
from email.message import EmailMessage




class Envoidemail():

  def __init__(self,port=465,smtp_server= "smtp.gmail.com",sender_email = "my@gmail.com",receiver_email = "your@gmail.com",password = "",object = "Hi there", content="This message is sent from Python."):
    fromaddr = sender_email
    toaddrs  = receiver_email
    self.SMTPServer = smtp_server
    self.port = port#465 #587
    self.login = sender_email
    self.password = password
    
    self.msg = EmailMessage()
    msgtxt = content
    self.msg.set_content(msgtxt)
    self.msg['Subject'] = object
    self.msg['From'] = sender_email
    self.msg['To'] = receiver_email
  def envoyer(self):
    try:
      #server = smtplib.SMTP_SSL(self.SMTPServer, self.port) #use smtplib.SMTP() if port is 587
      server = smtplib.SMTP()
      server.connect()
      #server.starttls()
      server.set_debuglevel(False)
      server.login(self.login, self.password)
      try:
        server.send_message(self.msg)
      finally:
        server.quit()
      return "l'envoi d'email s'est bien passé"
    except Exception as e:
      return "il y a eu une erreur"+str(e)

