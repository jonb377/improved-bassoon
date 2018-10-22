import os
import inspect
from porder import Set
from porder import _primes

os.system('vim gen_fn.py')

print('Reading gen_fn.py...')
exec(open('gen_fn.py').read())
print('gen_fn loaded!')

# This creates the set.
s = Set(gen_fn())

# Read in a number to evaluate the factorial of
while True:
    print('Enter a number: ', end='')
    n = int(input())
    print('{}! in the set provided is {}'.format(n, s.factorial(n)))
    print('\np-sequences:')
    s.print_sequences()
    print('\np-orderings:')
    s.print_orders()
    print('\nTotal values:', len(s.values))
