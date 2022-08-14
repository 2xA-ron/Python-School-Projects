#selection.py
# Program - Aaron Rodriguez
print('This program is a simple guessing game, your asked set of question and based on the response '
      'the response will vary if you got one or the other correct or nether correct.')

fav_color = input('\nGuess my friends color: ')
fav_number = int(input('\nGuess my friends favor number: '))

if fav_color == 'Yellow' and fav_number == 77: # These variables can be changed to have different outputs
    print("\nThat's correct! Yellow is the right favorite color.")
    print('\nAnd, 7 is the correct favorite number.\n')
elif fav_number=='Yellow' or fav_number ==77:
    print("\nHey, you entered the correct favorite color.")
    print("Or, you entered the correct favorite number.")
    print("However, you did not enter both\n")
else:
    print("\nYou entered neither Yellow nor 77.")

first_number = int(input('\nPlease enter first_number: ')) # User Input
second_number = int(input('\nPlease enter second number: '))

# Based on responses output will vary using the if, elif, and else
if first_number < second_number:
    print('\nAnswer {} < {}.\n'.format(first_number, second_number))
elif first_number > second_number:
    print('\nAnswer {} > {}.\n'.format(first_number, second_number))
else:
    print('\nAnswer {} == {}.\n'.format(first_number, second_number))

if (first_number < second_number) or (first_number > second_number):
    print("\nFirst number {} is not equal to "
    "Second number {}.\n".format(first_number, second_number))
else:
    print("\nFist number {} is equal to "
    "Second number {}.\n".format(first_number, second_number))