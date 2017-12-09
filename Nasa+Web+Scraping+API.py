
# coding: utf-8

# In[3]:

# The below imports the necessary packages from Python
# The request package will pull the json from the api
# The Mongo db database is setup to give a new database events
# Mime email and smtplib allow for emailing in gmail

from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
import csv
import numpy as np
import pandas as pd
import requests


from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.events

#Specify the ids that correspond to Landslides, Wildfire and Severe Storms
id=['8','10','14']

def get_events():
    for i in id:
        url="https://eonet.sci.gsfc.nasa.gov/api/v2.1/categories/"+i
        payload={'days':'31'}
        r=requests.get(url,params=payload)
        results = db.event.insert_one(r.json())
        curs = db.event.find({},{'events':1, 'events.id':1, 'events.title':1, 'events.geometries.date':1, 'events.geometries.coordinates':1})

#The below code creates a csv that can be read in excel and selects the relevant fields within MongoDb this loops through dictionaries within the query      
        
        with open('events.csv', 'w', newline='') as outfile:
            fields = ['_id', 'events.EONETid', 'events.title', 'events.date', 'events.coordinates']
            write = csv.DictWriter(outfile, fieldnames=fields)
            write.writeheader()
            for events_field in curs:
                events_id=events_field['_id']
                for events_field in events_field['events']:
                    events_geometries =events_field['geometries']
                    for event in events_geometries:
                        events ={
                                '_id':events_id,
                                'events.EONETid': events_field['id'],
                                'events.title': events_field['title'],
                                'events.date':event['date'],
                                'events.coordinates':event['coordinates']
                        }
                        write.writerow(events)
        
    
    
get_events()


emailfrom = "User_Email"   
emailTo = "Recpient_email"
password = "password"
msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailTo
msg["Subject"] = "Severe Storms, Wildfire and Eartquakes in the last Month"
msg.preamble = "Please find attached a csv of the results"


fp = open("events.csv")
attachment = MIMEText(fp.read())
fp.close()

attachment.add_header('Content-Disposition', 'attachment', filename="events.csv")           
msg.attach(attachment)


server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login(emailfrom,password)
server.sendmail(emailfrom, emailTo, msg.as_string())
server.quit()

