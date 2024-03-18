import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()
present_date =(f"{year}/{month}/{weekday}")

my_email = "delia.hudson@ethereal.email"
password = "c5wuCBqu21yenvZSVs"

if weekday == 3:
    with open("Quotes.txt", "r", encoding="UTF-8") as data:
        read_date = data.readlines()
        random_quote = random.choice(read_date)
        print(random_quote)

    with smtplib.SMTP("smtp.ethereal.email", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Works Now!\n\n {random_quote}".encode("utf8"))




