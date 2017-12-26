#wap t display cons and vowel in a string

s=input('enter a string')

for i in range(0,len(s)):
   
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        print("vowel=",s[i],end='')
    else:
        print('cosonant=',s[i],end='')

