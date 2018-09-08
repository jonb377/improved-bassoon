import math
from functools import reduce

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
        return self.__str__()


class Set(LazyList):
    '''
    The set to define the factorial over.
    '''
    def __init__(self, gen):
        super().__init__(gen)
        def p_sequence_gen(): # Define a generator for the p-sequence of each prime
            i = 0
            while True:
                yield LazyList(self.p_sequence(_primes.get(i)))
                i += 1
        self.p_sequences = LazyList(p_sequence_gen())

    def select_next_term(self, p, a, timeout=100):
        '''
        Approximately finds the next value in the p order / sequence.
        Empirically selects by examining the resulting product
            (a_i - a_0)(a_i - a_1)...(a_i - a_(i-1))
        for several elements in S and choosing the minimum-maximum power of
        p. Timeout parameter stops the search if the best hasn't been updated
        in the specified number of steps.
        
        This function might yield the wrong value if the optimal choice for a_i
        is large.
        
        Returns a_i and the associated power in the p-sequence.
        '''
        best = (float('inf'), -1, float('inf'))    # (index, a_i value, minpow)
        i = 0
        while i - best[0] < timeout:
            v = self.get(i)
            prod = reduce(lambda x, y: x * y, map(lambda x: v - x, a), 1)
            if prod == 0:
                timeout += 2 # Try to keep the timeout large enough
            else:
                minpow = highest_power_dividing(p, prod)
                if minpow < best[2]:
                    best = (i, v, minpow)
            i += 1
        return best[1:] # returns a_i and the power of p

    def p_sequence(self, p):
        '''
        Returns a generator for the p-sequence of the specified prime.
        '''
        a = [] # The p-ordering
        while True:
            a_i, power = self.select_next_term(p, a)
            a.append(a_i)
            yield power

    def print_sequences(self):
        '''
        Print the current values for the p-sequences
        '''
        for i in range(len(self.p_sequences.values)):
            print(_primes.get(i), self.p_sequences.get(i))

    def factorial(self, x):
        '''
        Evaluates the factorial over this set.
        '''
        i = 0
        fact = 1
        while self.p_sequences.get(i).get(x) > 1:
            fact *= self.p_sequences.get(i).get(x)
            i += 1
        return fact


def highest_power_dividing(p, value):
    '''
    Returns the highest power of p that divides the specified value
    '''
    if value == 0:
        return float('inf')
    power = 1
    while value % (power * p) == 0:
        power *= p
    return power

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

def square_gen():
    '''
    A generator for square numbers
    '''
    i = 0
    while True:
        i += 1
        yield i * i

if __name__ == '__main__':
    # If this is the main program, run the square number set
    s = Set(prime_gen())
    print('Enter a number for factorial: ', end='')
    n = int(input())
    print('\n{}! in set of squares is {}\n'.format(n, s.factorial(int(n))))
    print('The p-sequences used are:')
    s.print_sequences()