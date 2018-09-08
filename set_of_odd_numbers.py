from porder import Set

# The set needs an infinite generator
def odd_gen():
    '''
    This is a generator for odd numbers.
    '''
    i = 1
    while True: # The generator is infinite since this never terminates
        yield i
        i += 2  # Move to the next odd number

# This creates the set.
s = Set(odd_gen())

# Now the set is ready to evaluate the factorial.
five_factorial = s.factorial(5)

print('5! in the set of odd numbers is {}\n'.format(five_factorial))

# Read in a number to evaluate the factorial of
print('Enter a number: ', end='')
n = int(input())
print('{}! in the set of odd numbers is {}'.format(n, s.factorial(n)))
s.print_sequences()
