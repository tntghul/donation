from flask_mail import *


class Email:
    def __init__(self,app):
        #-------------------mail configuration---------------------------
        app.config["MAIL_SERVER"]='smtp.office365.com'
        app.config["MAIL_PORT"] = 587
        app.config["MAIL_USERNAME"] = 'priyansi234@outlook.com'
        app.config["MAIL_PASSWORD"]= 'tktkzywfkxflxumi'
        app.config["MAIL_USE_TLS"] = True
        app.config["MAIL_USE_SSL"] = False
        self.mail = Mail(app)  #mail object
#----------------------------------------------------------
    def compose_mail(self,subject,email,message):
        msg = Message(subject,
                    sender ='priyansi234@outlook.com',
                    recipients = [email])
        msg.body = message
        self.mail.send(msg)

   