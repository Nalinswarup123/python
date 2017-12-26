#return longest common prefix of two string if no common then returns empty

def pre(a,b):
    c=''
    for i in range(len(a)):
            if(a[i]==b[i]):
                c=c+a[i]
            else:
                break
    return c
print(pre(input(),input()))
            
                
