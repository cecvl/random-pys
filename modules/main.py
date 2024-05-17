# create objects from classes in imported modules
import datetime, random , bday_messages

# Q: use datetime module to create today object
# A: today = datetime.date.today()
# year, month, day
today = datetime.date.today()
print(today)

birthday = datetime.date(2005, 6, 3)
print(birthday)

age = today.year - birthday.year
print(age)

# calculate days to the next birthday using two objects
next_birthday = datetime.date(today.year, birthday.month, birthday.day)

# Q: how do i calculate the total number of days until the next birthday?
# A: You can calculate the total number of days until the next birthday by subtracting today's date from the next birthday date. Here's an example:
# Q: nope, that wont work
# A: You're right! The previous approach won't work because the next birthday date might be in the past if the birthday has already occurred this year. You can handle this case by checking if the next birthday date is before today's date and adjusting the year accordingly. Here's an updated approach:
# A: if next_birthday < today:
# A:     next_birthday = next_birthday.replace(year=today.year + 1)
# A: days_away = (next_birthday - today).days
# A: print(days_away)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_away = (next_birthday - today).days

message = random.choice(bday_messages.messages)
if today == next_birthday:
    print(message)
else:
    print(f"{(days_away)} days until your next birthday!")