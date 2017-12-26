def fun():
    print('some output')
a=10
b=0
result=None
try:
    result=a/b
    print(result)
except Exception:
    fun()
    raise
