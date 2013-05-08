# This will work with flat lists of hashable types
# doesn't check order hence they are 'similar' or contain
# the same items
def identical(l1, l2):
    return len(l1) == len(l2) and set(l1) == set(l2)
