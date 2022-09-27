## Imports

import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.message import Message
from email.mime.text import MIMEText

## Mail Sending function

def mailsend(emailto):

  ## Mail details

  emailfrom = "ytscrapercommentps@gmail.com"
  fileToSend = ["Full Comments.csv", "Positive Comments.csv", "Negative Comments.csv"]
  username = "ytscrapercommentps@gmail.com"
  password = "PASSWORD"

  ## Mail Subject

  msg = MIMEMultipart()
  msg["From"] = emailfrom
  msg["To"] = emailto
  msg["Subject"] = "Hi your youtube comments excel file is here   -Youtube Comment Scraper"
  # msg.preamble = "Hi your csv file is ready from  -Youtube Comment Scraper"

  ## Adding attachments

  subtype = 'vnd.ms-excel'  # Subtype for excel or csv files
  for f in fileToSend:
    fp = open(f, encoding = 'utf8')
    attachment = MIMEText(fp.read(), _subtype = subtype)
    fp.close()
    attachment.add_header("Content-Disposition", "attachment", filename=f)
    msg.attach(attachment)

  ## Sending mail to the user

  server = smtplib.SMTP("smtp.gmail.com:587")
  server.starttls()
  server.login(username,password)
  server.sendmail(emailfrom, emailto, msg.as_string())
  server.quit()
