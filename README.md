# Description
**Youtube Comment Scraping and Analysis:**  It is a web application made specially for youtube content creators to know their reviews separately as positive and negative comments.

# Working Video
https://drive.google.com/file/d/1x-bNAR4Snt1Yz-9nurBKiu96nMXcbQZL/view?usp=share_link

# What it does
- Asks for youtube video url and mail id.
- The web application scrapes the comments of the video and analyses the positive and negative comments.
- The time for scraping the comments depends on how many comments in the video. The estimate is that, it takes about 5 to 6 minutes to scrap 1000 comments.
- After the process is complete, the comments are mailed to the mail-id given by the user, as a excel file.
- Three files will be sent to the mail-id:
  - Full comments
  - Positive comments
  - Negative comments
- It will also produce a HTML table when the process is finished in the background.
- There are two tables: Positive Comments Table and Negative Comments Table.

# Build Status
- The web app will work without any bugs in local machine and produce the output.
- **BUG** - When run on the cloud, the website does not work for the video url that takes time more than 30 seconds to scrap the comments.
- The bug is due to the built of cloud to produce timeout error after 30 seconds.

# To-Do's
- NLTK used is Vader lexican module, it can be improved by our own NLTK model in machine learning or Deep Learning (Ex: BERT) but the downside is that, we have to collect labelled data to train the model. So, for now Vader lexican module is used.
- **BUG FIX:** Make the program to stop the scraping and produce the table with the comments that are scraped so far, for every 20 seconds until the scraping is finished fully. (I am new to cloud, not sure if it will work.)
- Try youtube API for faster comment scraping.
- If we cannot able to fix the bug, we can make a normal application to run on the local systems(PC Application).

# How to run on local machine
- Unnecessary files – Procfile, nltx.txt, requirements.txt, runtime.txt.
- **NOTE :** If the bug is fixed and you want to run on cloud, these files are necessary.
- Run the codes in your preferred IDE [I used PyCharm Professional]. It will run fine on local machine.

# Mail Sending File Changes
- Changes to be done in mail_sending_to_user_with_attached_csv_files.py
- Create one Gmail ID for sending emails to the user.
- **NOTE:** Do not use the password you created when opening the mail-id.
- After Creating Gmail id, Create your App Password and use this generated password in the program, so that google enables you to sign in via bot.
- Steps to Create App password:
  - Go to manage your google account -> Go to Setting -> Scroll down to find Signing in to Google -> Click App passwords -> Enter password -> Generate your App password.
- Change Subject of your wish.
