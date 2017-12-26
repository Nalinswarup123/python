class item(object):
    def __init__(self,n,v,w):
        self.name=n
        self.value=float(v)
        self.weight=float(w)
    def getname(self):
        return self.name
    def getvalue(self):
        return self.value
    def getweight(self):
        result='<'+self.name+','+str(self.value)+','+str(self.weight)+'>'
        return result
def value(item):
    return item.getvalue()
def weightinverse(item):
    return 1.0/item.getweight()
def density(item):
    return item.getvalue()/item.getweight()
def builditems():
    
    names=['clock','painting','radio','vase','book','computer']
    values=[175,90,20,50,10,200]




def testgreedy(items,constrait,keyfunction):
    taken,val=greedy(items,constrains,keyfunction)
    print('total value of items takens',val)
    for items in taken:
        print(' ',item)
def testgreedys(a):
    maxweight=a
    items=builditems()
    print()
