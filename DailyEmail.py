import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import GetData as email_content
import json
import base64
from datetime import datetime
import EncryptDecrypt as ed

import smtplib
from email.message import EmailMessage



class DailyEmail():
    

    def __init__(self):

        config_filename = "config.txt"

        #decrypt the config file
        key = ed.load_key()
        ed.decrypt(config_filename, key)
    


    def send_email(self):
        msg = EmailMessage()
        msg['Subject'] = 'Here is my newsletter'
        msg['From'] = "dkguruge@gmail.com"
        msg['To'] = "dulminiguruge@gmail.com"
        msg.set_content(self.format_email, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("dkguruge@gmail.com", "euti aslg ywlj qngg") 
            smtp.send_message(msg)
            

    def format_email(self):
        weather =email_content.GetAPIData.get_weather_forecast
        #events = email_content.GetAPIData.get_google_calender_api
       

        msg = '''
        <!DOCTYPE html>
        <html>
            <body>
                <div style="background-color:#eee;padding:10px 20px;">
                    <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">My newsletter</h2>
                </div>
                <div style="padding:20px 0px">
                    <div style="height: 500px;width:400px">
                        <img src="https://dummyimage.com/500x300/000/fff&text=Dummy+image" style="height: 300px;">
                        <div style="text-align:center;">
                            <h3>Article 1</h3>
                            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. A ducimus deleniti nemo quibusdam iste sint!</p>
                            <a href="#">Read more</a>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        '''

        return msg


        