'''biologists use seq of letter ACTC to model a genome. A gene is a substring
of gnome that starts after triplet ATG and ends before triplet TAG , TAA and
TGA.
the length of Gene string is mul of 3 and Gene doesnot contain any of the triple
TAG , TAA and TGA.
wap to ask user to enter a genone and display all genes in genone.
if no gene is found in seq then display no gene found.'''

s=input('enter model')

for i in range(len(s)):
    if(s[i:i+3]=="ATG"):
        for j in range(i+3,len(s)):
            if(s[j:j+3]!="TAG" or s[j:j+3]!="TAA" or s[j:j+3]!="TGA"):
                print(s[i+3:j])
    else:
        print('no gene found')

