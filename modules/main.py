# create objects from classes in imported modules
import datetime, bday_messages

# Q: use datetime module to create today object
# A: today = datetime.date.today()
# year, month, day
today = datetime.date.today()
birthday = datetime.date(2004, 5, 1)

age = today.year - birthday.year
print(age)