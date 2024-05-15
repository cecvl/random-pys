# create objects from classes in imported modules
import datetime, bday_messages

# Q: use datetime module to create today object
# A: today = datetime.date.today()
# year, month, day
today = datetime.date.today()
print(today)

birthday = datetime.date(2005, 4, 5)
print(birthday)

age = today.year - birthday.year
print(age)

# calculate days away from next birthday
next_birthday = datetime.date(today.year, birthday.month, birthday.day)
print(next_birthday)

days_away = (next_birthday - today).days

if today == next_birthday:
    print("Happy Birthday!")
else:
    print(f"{(days_away)} days until your birthday!")