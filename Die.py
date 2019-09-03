from random import randint

class Die():
    ''' Create and roll die. '''

    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        self.list_of_rolls = []
        self.freq_list = []

    def roll(self, num_rolls=1):
        ''' Roll the die and add result to list of rolls. '''
        for i in range(num_rolls):
            self.list_of_rolls.append(randint(1,self.num_sides))

    def roll_stats(self):
        ''' Calculate frequency of each result. '''
        for i in range(1,self.num_sides+1):
            self.freq_list.append(self.list_of_rolls.count(i))