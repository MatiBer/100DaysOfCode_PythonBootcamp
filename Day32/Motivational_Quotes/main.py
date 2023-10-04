import smtplib
import datetime as dt
import random

my_email = "mateusz.berlinski7@gmail.com"
password = ""

now = dt.datetime.now()
current_weekday = now.weekday()

if current_weekday == 0:
    with open("quotes.txt", "r") as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mateusz.berlinski7@yahoo.com",
                            msg=f"Subject:Motivational Quote\n\n{quote}")