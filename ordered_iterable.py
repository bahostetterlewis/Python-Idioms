# where s is an iterable
if sorted(s) == list(s):
    print('Elements were sorted')
else:
    print('Elements were not sorted')


# In general if you want to check if an iterable is sorted... just sort it
# This method runs in O(n) time.
from itertools import imap, tee
import operator

def is_sorted(iterable, compare=operator.le):
  a, b = tee(iterable)
  next(b, None)
  return all(imap(compare, a, b))
