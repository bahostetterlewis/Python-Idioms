# utilizes pythons automatic file closing
max(open('sometfile.txt', 'r'), key=len)

# better but not as short (forces file close explicitly)
with open('somefile.txt', 'r') as f:
    max(f, key=len)
