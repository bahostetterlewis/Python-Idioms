# from 2 lists
keylist = ['k1', 'k2', 'k3']
vallist = ['v1', 'v2', 'v3']
d = dict(zip(keylist, vallist))

# from iterable of tuples, note this is with a list but works with any iterable of tuples
kvs = [('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')]
d = dict(kvs)
