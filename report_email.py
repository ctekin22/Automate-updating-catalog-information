#!/usr/bin/env python3
from datetime import date
import os
import requests
from reports import generate_report
from emails import generate_email, send_email 


if __name__ == "__main__":
    paragraph="./supplier-data/descriptions/"         
    title = "Processed Update on {}.".format(date.today().strftime("%B %d, %Y"))
    attachment="/tmp/processed.pdf"
    body=""
    for file in os.listdir(paragraph):
        with open(paragraph + file, "r") as f:
            body = body + "name: " + f.readline().strip()+"<br/>"
            body = body + "weight: " + f.readline().strip() +"<br/>"
            body = body + "<br/>"
            generate_report(attachment,title,body)
 
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get("USER"))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"
    send_email(generate_email(sender, receiver, subject, body, attachment))
