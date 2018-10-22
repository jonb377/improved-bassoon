class LazyList:
    '''
    A list that is lazily generated.
    '''
    def __init__(self, gen):
        self.gen = gen
        self.values = []

    def __getitem__(self, i):
        '''
        Returns the item at the ith index in the list.
        '''
        while i >= len(self.values):
            self.values.append(next(self.gen))
        return self.values[i]

    def __str__(self):
        return str(self.values)[:-1] + ', ...]'
    def __repr__(self):
        return str(self)
