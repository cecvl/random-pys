#Define a function named fortune(). Inside the function, print out a random fortune from the list of options

import random
def fortune():
    fortunes = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
    print(random.choice(fortunes))
# Q:explain: print(random.choice(fortunes))
# A: The random.choice() method returns a randomly selected element from the specified sequence. In this case, it selects a random fortune from the list of options and prints it out.
# Q: can we use another method instead of choice()
# A: Yes, you can use the random.randint() method to generate a random index and then access the corresponding fortune from the list. Here's an example:
# A: index = random.randint(0, len(fortunes) - 1)
# A: print(fortunes[index])

def fortunetell():
    fortune = ["Don't pursue happiness – create it.", "All things are difficult before they are easy.", "Don't just think. Act!"]
    index = random.randint(0, len(fortune) - 1)
    print(fortune[index])

fortune()
fortunetell()
