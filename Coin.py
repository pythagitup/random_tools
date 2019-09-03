from random import choice

class Coin():
    '''Create and flip a coin. '''

    def __init__(self, num_flips=1):
        self.faces = ['Heads', 'Tails']
        self.num_flips = num_flips
        self.list_of_flips = []
        self.freq_list = []

    def flip(self):
        ''' Flip the coin and add results to list. '''
        for i in range(self.num_flips):
            self.list_of_flips.append(choice(self.faces))

    def flip_stats(self):
        ''' Calculate frequency of each flip result. '''
        self.freq_list.append(self.list_of_flips.count('Heads'))
        self.freq_list.append(self.list_of_flips.count('Tails'))
