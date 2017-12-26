def contains(string,char):
    for  i in range(len(string)-1,-1,-1):
        if string[i]==char:
            print(char)
            return i
    raise ValueError('could not find %r in %r'%(char,string))
try:
    contains('baabab','a')
except ValueError:
    print('abc')
    raise ValueError('could not find %r in %r'%(char,string))

