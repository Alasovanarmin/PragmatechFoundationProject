"""Tapsiriq 01 def showFilteredNumbers():
a=input('eded daxil edin : ')
b=input('eded daxil edin : ')

def showFilteredNumbers():
    try:
        int(a)
        int(b)
        return True
    except:
        print("duzgun deyer daxil edilmeyib")
print(showFilteredNumbers())
    """  

"""def showFilteredNumbers1():
    if b<a:
        return True 
    else:
        print("Daxil edilen deyerler teleblere uygun deyil")
        
showFilteredNumbers1()
"""
"""def showFilteredNumbers2(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        return "Duzgun deyer daxil edilmeyib"
    elif a<b:
        print("Daxil edilen deyerler teleblere uygun deyil")
    elif a>b:
        for i in range(b,a):
            if i % 5 ==0 and i % 7 !=0:
                print(i)
print(showFilteredNumbers2(20,3))
    """    
    
    
     
    
"""" Tapsiriq 02 
def sumofNumbers(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        return "Duzgun deyer daxil edilmeyib"
    sum=0
    for i in range(a,b):
        sum+=i
    return sum
print(sumofNumbers(5,20))
"""      


""" #Tapsiriq 03 
def findMiddleNumber(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
      return "Duzgun deyer daxil edilmeyib"
    avgNumber = (a+b)/2
    for i in range(1,100):
       if i>avgNumber:
        print(i)
findMiddleNumber(5,10)    """      



     
     
"""def getNumbers(a):
    for i in str(a):
        print(i)
        
print(getNumbers(88758))
"""      





"""
def getCountNumbers(a):
    count=0
    for i in str(a):
        count+=1
        return count
print(getCountNumbers(8878))   """ 



"""def sum(a):
    sum=0
    for i in str(a):
        sum+=int(i)
        return sum
print(sum(88758)) 
"""      


"""def func():   # sahmat meselesi
    x=range(1,65)
    a=1
    for n in x:
        a=a*2
        print(a)
        
print(func())"""



    



