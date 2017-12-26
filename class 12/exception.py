def main():
    while True:
        try:
            n1,n2=eval(input('enter two nos'))
            res=n1/n2
            print('result=',res)
        except ZeroDivisionError:
            print('div by 0 is not allowed')
        except SyntaxError:
            print('syn error')
        except:
            print('input error')
        else:
            print('else')
        finally:
            print('final clause is executed')
            break
            
    
main()
