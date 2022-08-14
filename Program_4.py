# program 4
print('This is Program 4, Aaron Rodriguez ')
print("\nThis program sets the user up to select their PriorityStatus, Prefernece in seating, as well as the budget they are working with," 
    "\nfrom there the program demestrates getting different feedback scenerios based on overall scores of satisfaction from your flight experience. ")


# User details
print("\nThis program provides airline seat assignment ")
print("\nEnter the following information about yourself ")

# info
firstName = input("First name : ")
lastName = input("Last name  : ")
priorityStatus = input("Priority Status (Platinum, Gold, Newbie) : ")
seatPreference = input("Seat Preference (First Class, Business, Coach) : ")
ticketBudget = input("Ticket Budget(Colossal, Big Bucks, Peanuts):")

# Platinum and ticketBudget is Colossal
if priorityStatus == "Platinum" and ticketBudget == "Colossal":
    print("\n", firstName, ' ', lastName, "You qualify for First Class and they are exceptional seats! ")

if "Platinum" == priorityStatus and ticketBudget == "Big Bucks":
    print("\n", firstName, " ", lastName, """You have Business and they are okay seats. We suggest you spend more"
        "money to get better seats. """)
# Platinum and ticketBudget is Peanuts
if priorityStatus == "Platinum" and ticketBudget == "Peanuts":
    print("\n", firstName, " ", lastName, "Really? You are in Coach and will be sorry.")

if priorityStatus == ("Gold" and ticketBudget == "Colossal"):
    print("\n", firstName, " ", lastName, "You qualify for First Class. Did you get the promotion? ")
# Gold and ticketBudget is Big Bucks
if priorityStatus == ("Gold" and ticketBudget == "Big Bucks"):
    print("\n", firstName, " ", lastName, "You have Business, as usual. You know we do recommend First Class!")
# Gold and ticketBudget is Peanuts
if priorityStatus == ("Gold" and ticketBudget == "Peanuts"):
    print("\n", firstName, " ", lastName, "Really? You can do better do you think?")

# Gold and ticketBudget is Colossal
if priorityStatus == "Newbie" and ticketBudget == "Colossal":
    print("\n", firstName, " ", lastName, "We are running your credit again to ensure there are no mistakes."
                                          "Looks like you may get First Class. Please behave. ")
# Gold and ticketBudget is Colossal
if priorityStatus == "Newbie" and ticketBudget == "Big Bucks":
    print("\n", firstName, " ", lastName, 'Hm..Our fashion consultant will ensure you\'re professionally'
                                          'dressed if so, it is Business for you!')
# Gold and ticketBudget is Colossal
if priorityStatus == "Newbie" and ticketBudget == "Peanuts":
    print("\n", firstName, " ", lastName, "We apologize in advance for the crying baby next to you."
                                          "Please limit peanut request to one 1 oz. bag.")
# Rate experience
print("\nRate your experience on the scale of 1 - 5 (1 = dissatisfied; 5 = outstanding) ")

flight = int(input(" Did you have a good flight? : "))
food = int(input(" Was the food fantastic? : "))
movie = int(input("How was the movie selection? : "))

overAllScore = flight + food + movie

# Platinum status
# noinspection PyTypeChecker
if priorityStatus.lower() == "platinum" and (overAllScore < 12 or flight < 4 or food < 4 or movie < 4):
    print("Your survey score of", overAllScore,
          "was lower than we would like. Please give us another opportunity soon.")

if priorityStatus.lower() == "gold" and (overAllScore < 11 or flight < 3 or food < 3 or movie < 3):
    print("Your survey score of", overAllScore,
          'was lower than we would like. The next time you fly you receive a complementary soft drink.')

if priorityStatus.lower() == "newbie" and (overAllScore < 10 or flight < 2 or food < 2 or movie < 2):
    print("Your survey score of", overAllScore, "was lower than we would like. You will have more fun next time.")
print("""\n The this program was fun but challenging at the same time."
      " I was trying to remember how the IF and ELIF statements get written for each piece of information."
      "However as I went through the process of figuring out how"
    "to write this code it became easier as this writing of the program is alot of repetition. "
      "I stumbled on a couple errors towards the end. I trying to learn as i go nonetheless.""")
