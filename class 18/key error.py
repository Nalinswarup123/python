values={'a':1,'b':2}
print(values.get('b'))
try:
    print(values['c'])
except LookupError:
    print('keyerror encounter')
    raise

