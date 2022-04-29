import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
from rightmove_webscraper import RightmoveData
import pandas as pd




email_sender_account = "" # User Email
email_sender_username = "" # Email username username@gmail.com
email_sender_password = "" # email password
email_smtp_server = "" # smtp server for gmail = smtp.gmail.com
email_smtp_port = 587 # gmail smpt port = 587
email_recepients = [""] #email recepients
email_subject = "New Property on RightMove"
refresh_period = 30 # interval applicaiton checks rightmove (minutes)
url = "" # Rightmove search url

rm = RightmoveData(url)
res = rm.get_results
num = len(res)
print('Original number of listings:', num)

def CheckRightMove():
    global res, num, rm

    old_num = num
    original_res = res

    rm = RightmoveData(url)
    res = rm.get_results
    res = res.drop(columns='search_date')

    try:
        original_res = original_res.drop(columns='search_date')
    except:
        print('')

    num = len(res)
    print('previous number of listings:', old_num)
    print('new number of listings:', num)

    if num != old_num:

        # login to email server
        server = smtplib.SMTP(email_smtp_server, email_smtp_port)
        server.starttls()
        server.login(email_sender_username, email_sender_password)  # For loop, sending emails to all email recipients

        #Identify differences between new and old requests
        df = pd.concat([res, original_res]).drop_duplicates(keep=False)

        # Send to each recipient
        for recipient in email_recepients:
            print("Sending email to:", recipient)
            message = MIMEMultipart('alternative')
            message['From'] = email_sender_account
            message['To'] = recipient
            message['Subject'] = email_subject
            html = """\
            <html>
              <head></head>
              <body>
                {0}
              </body>
            </html>
            """.format(df.to_html())
            message.attach(MIMEText(html, 'html'))
            text = message.as_string()
            server.sendmail(email_sender_account,recipient,text)#All emails sent, log out.

        server.quit()

#schedule checking of Rightmove website
schedule.every(refresh_period).minutes.do(CheckRightMove)


while True:
    schedule.run_pending()
    time.sleep(1)

