import datetime as dt
import pandas as pd
import random
import smtplib

# 1. Update the birthdays.csv with your friends & family's details.

#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# ---------------You can do it using python index or using pandas module like below:-----------------------
        #with open("birthdays.csv") as data:
            #read_data = data.readlines()

# Extract the birthday date from the csv file to save to a variable.
#birthday_date = read_data[2][35:47]
        #birthday_date_list = birthday_date.split(",")
        #print(birthday_date_list)
        #birthday_year = int(birthday_date_list[0])
        #birthday_month = int(birthday_date_list[1])
        #birthday_day = int(birthday_date_list[2])
        #birthday_tuple = (birthday_year, birthday_month, birthday_day)

# HINT 1: Create a tuple from today's month and day using datetime. e.g.
now = dt.datetime.now()
now_month = now.month
now_day = now.day
now_tuple = (dt.datetime.now().month, dt.datetime.now().day)

# HINT 2: Use pandas to read the birthdays.csv
data = pd.read_csv("birthdays.csv")

name_test = data.iloc[0, 0]
year_test = data.iloc[0, 2]
month_test = data.iloc[0, 3]
day_test = data.iloc[0, 4]
test_birthday = data.iloc[0].values
print(test_birthday)


# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
birthdays_dict = {
    (day_test, month_test): test_birthday
}
print(birthdays_dict)

#new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if now_tuple in birthdays_dict:
    print("It is my birthday")

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
    with open("letter_templates/letter_1.txt") as data_letter1, \
         open("letter_templates/letter_2.txt") as data_letter2, \
         open("letter_templates/letter_3.txt") as data_letter3:
        letter1 = data_letter1.read()
        letter2 = data_letter2.read()
        letter3 = data_letter3.read()

# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp
    letter1_name = letter1.replace("[NAME]", name_test)
    letter2_name = letter2.replace("[NAME]", name_test)
    letter3_name = letter3.replace("[NAME]", name_test)

# HINT 2: Use the random module to get a number between 1-3 to pick a random letter.
    letters = [letter1_name, letter2_name, letter3_name]
    random_letter = random.choice(letters)


# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.


    with smtplib.SMTP("smtp.ethereal.email", port=587) as connection:
        connection.starttls()
        connection.login(user="russ60@ethereal.email", password="NCQ1v3ZWBRTnTHt8ct")
        connection.sendmail(
            from_addr="russ60@ethereal.email",
            to_addrs="russ60@ethereal.email",
            msg=f"Subject:Happy Birthday!\n\n {random_letter}".encode("utf8"))

