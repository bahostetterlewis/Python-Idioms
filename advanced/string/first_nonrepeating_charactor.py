from collections import Counter

def first_non_repeating(string):
    ''' 
    Find the first charactor in a string that is not repeated.
    
    Filters all potential charactors and then finds the first of those characters
    in the given string.
    '''
    unique = (char for char,count in Counter(string).items() if count == 1) #  create a generator to provide all non repeated chars
    try:
        location = min(string.find(char) for char in unique)  # find the location of first unique
    except ValueError:
        return ''  # This is returned when all charactors are duplicates
    return string[location]
