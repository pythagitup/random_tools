from random import choice

class Coin():
    '''Create and flip a coin. '''

    def __init__(self, num_flips=1):
        self.faces = ['Heads', 'Tails']
        self.num_flips = num_flips

    def flip(self):
        ''' Flip the coin once and print result. '''
        for i in range(self.num_flips):
            result = choice(self.faces)
            print(f'\t{result}')
