class LazyList:
    '''
    A list that is lazily generated.
    '''
    def __init__(self, gen):
        self.gen = gen
        self.values = []

    def get(self, i):
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


def prime_gen():
    '''
    A generator for prime numbers. Only works in conjunction with the global
    _primes LazyList.
    Quite inefficeint but it gets the job done
    '''
    curr = 1
    # Essentially just find the next number that isn't divisible by a known prime
    while True:
        curr += 1
        for p in _primes.values:
            if curr % p == 0:
                break
        else:
            yield curr

_primes = LazyList(prime_gen()) # A lazy list of primes
