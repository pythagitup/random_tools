from random import randint

class Die():
    ''' Create and roll die. '''

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self, num_rolls=1):
        ''' Roll the die and print the result. '''
        for i in range(num_rolls):
            result = randint(1,self.num_sides)
            print(f'\t{result}')
