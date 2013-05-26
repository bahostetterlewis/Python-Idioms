from collections import Counter

def first_non_repeating(string):
    ''' 
    Find the first charactor in a string that is not repeated.
    
    Filters all potential charactors and then finds the first of those characters
    in the given string.
    '''
    unique = (char for char,count in Counter(string).items() if count == 1) #  create a generator to provide all non repeated chars
    try:
        return min(unique, key=string.find)  # find the first non duplicated char
    except ValueError:
        return ''  # This is returned when all charactors are duplicates
