# List comprehensions/dict comprehensions/ generators
# offer an easy way to simulate mathematical set notation
# when generating, transforming, or manipulating iterables
# The three primary comprehensions are list, dict, and generator
# Used properly these can replace nearly every use of map/filter in python

# Form is similar to A = {i^2 | i ∋ ℕ)
# This means that the set A is made up of all squares of the natural numbers
# Comprehensions can create the same values with the following syntax
# A = (i*i for i in itertools.count()) 


# List comprehensions are commonly used to generate a list when size is known
# and all elements are used at once. It is important to note that all values
# are generated and then returned, don't use infinite sequences for these!
finite_squares = [i*i for i in range(10)]  # reads: i squard for every i in range 0-9
                                           # generates the list [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dict comprehensions are commonly used to generate modified dictionaries from other dictionaries
# Or to map some initial value to a modified value
# Just like list comprehensions these are generated at once so don't use infinite sequence

# First, an example of mapping values. Lets map squares to their root from 0-9
d = {i*i:i for i in range(10)}  # reads: i*i maps to i for every i in range 0-9
                                # generates the dictionary {0: 0, 1: 1, 4: 2, 49: 7, 16: 4, 25: 5, 64: 8, 9: 3, 81: 9, 36: 6}

# Next an example of transforming one dict into another
# Here we want to reverse a dict so that its values are now the keys and vice versa
d = {'key1':'val1', 'key2':'val2', 'key3':'val3'}
d = {d[k]:k for k in d}  # reads: value at key k maps to k for k in the dictionary
                         # generates the dictionary {'val1': 'key1', 'val3': 'key3', 'val2': 'key2'}


# Generators are a special form of comprehension. They allow for the creation of
# what is effectively a "co-routine".
# They allow for manipulating infinite sequences and offer lazy evaluation.
# This means that they will generate each number only when requested.
# This gives them a small memory footprint only one value is created at a time
# and it never stores previous values.

# Using parens around a comprehension creates a generator
from itertools import count
a = (i*i for i in count())  # this is an infinite generator that returns every square
                            # reads: i squared for every i in the count (count generates infinite positive integers

# All the above notations have used the map capabilities of comprehensions but they also have a filter 
a = (i*i for range(100) if i % 2 == 0)  # creates a generator
                                        # reads: i squared for every i in the range 0-99 if i is even
