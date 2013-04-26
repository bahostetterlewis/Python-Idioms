# from 2 iterables
keylist = ['k1', 'k2', 'k3']
vallist = ['v1', 'v2', 'v3']
d = dict(zip(keylist, vallist))

# from iterable of tuples, note this is with a list but works with any iterable of tuples
# also note they don't have to be tuples a list of lists works here as well
kvs = [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')]
d = dict(kvs)

# explicit creation
d = {'k1':'v1', 'k2':'v2', 'k3','v3'}
