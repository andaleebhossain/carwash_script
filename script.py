import csv
import datetime
from datetime import date
import smtplib
from email.message import EmailMessage

today_date = date.today()
name = ''

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        test = row[1]
        test = test.replace('-', ' ')
        test_date = datetime.datetime.strptime("{0} 2023".format(test), "%d %b %Y").strftime("%Y-%m-%d")
        if str(today_date) == str(test_date):
            name = row[3]

test_body = 'Hey ' + name + ',\nIt is your turn to wash your car today!'

db = {
    'Nafees Hossain': 'nafeeshossain535@gmail.com',
    'Ronald Thomas' : 'ronthomas.ca@gmail.com',
    'Azad Bhai' : 'mmtksa@gmail.com',
    'Shamsul Alam' : 's_alam101@yahoo.com'
}

user = 'wcar53238@gmail.com'
password = 'ohgqihicvnpbrnii'

msg = EmailMessage()

msg.set_content(test_body)
msg['subject'] = 'Car Wash Reminder'
msg['to'] = db[name]
msg['from'] = user

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user, password)
server.send_message(msg)

server.quit()