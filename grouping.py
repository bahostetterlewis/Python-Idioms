from collections import defaultdict

def grouper(iterable, key=lambda x: x):
  ''' Group an iterable by some key function.
  
  By default this groups based on value.
  ie: all key and value pairs will be identical.
  
  Required arguments:
  iterable -- an iterable object
  
  Keyword arguments:
  key -- function to be called on each element, determines what is grouped by
  
  returns a defaultdict of key's and value lists containing the groups
  '''
  result = defaultdict(list)
  for it in iterable:
    result[key(it)].append(it)
    
  return result
