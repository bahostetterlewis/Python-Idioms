s = input('give me a string')

if len(s) == len(set(s)):
  print('all characters unique')
else:
  print('not all characters were unique')
