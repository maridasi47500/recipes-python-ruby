import smtplib, ssl
class Envoidemail():

  def __init__(self,port=587,smtp_server= "smtp.gmail.com",sender_email = "my@gmail.com",receiver_email = "your@gmail.com",password = "",message = """\\nSubject: Hi there\nThis message is sent from Python."""):
    self.port = port  # For starttls
    self.smtp_server = smtp_server
    self.sender_email = sender_email
    self.receiver_email = receiver_email
    self.password = password 
    self.message = message 

    self.context = ssl.create_default_context()
  def envoyer(self):
    with smtplib.SMTP(self.smtp_server, self.port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=self.context)
        server.ehlo()  # Can be omitted
        server.login(self.sender_email, self.password)
        server.sendmail(self.sender_email, self.receiver_email, self.message)

