from Coin import Coin
from Die import Die
from Card import Card

print('Welcome to Random Tools.')

while True:
    print('\nWhat would you like to do?\n\t(1) Roll a die\n\t(2) Flip a coin\n\t(3) Draw a card\n\t(4) Quit')

    choice = input('Enter your choice here: ')
    
    if choice == str(1):
        num_sides = input('How many sides should the die have? ')
        num_sides = int(num_sides)
        if num_sides >= 3:
            num_rolls = input('How many times do you want to roll the die? ')
            num_rolls = int(num_rolls)
            if num_rolls >= 1:
                die1 = Die(num_sides)
                die1.roll(num_rolls)
            else:
                print('Sorry, you have to roll the die at least once!')
        else:
            print('Sorry, the die must have at least 3 sides!')
    elif choice == str(2):
        num_flips = input('How many times do you want to flip the coin? ')
        num_flips = int(num_flips)
        if num_flips >= 1:
            coin1 = Coin(num_flips)
            coin1.flip()
        else:
            print('Sorry, you have to flip the coin at least once!')
    elif choice == str(3):
        num_draws = input('How many cards do you want to draw? ')
        num_draws = int(num_draws)
        if 1 <= num_draws <= 52:
            card1 = Card(num_draws)
            card1.draw()
        elif num_draws < 1:
            print('Sorry, you have to draw at least one card!')
        else:
            print('Sorry, that\'s more than the number of cards in the deck!')
    elif choice == str(4):
        print('Goodbye.')
        break
    else:
        print('\tSorry, I didn\'t understand you!')