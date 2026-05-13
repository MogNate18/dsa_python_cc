def funcA(n):
 if n > 0:
  print("A:", n)
  funcB(n - 1)

def funcB(n):
 if n > 0:
  print("B:", n)
  funcC(n - 1)
  
def funcC(n):
    if n > 0:
     print("C:", n)
     funcD(n-1)
     
def funcD(n):
    if n > 0:
     print("D:", n)
     funcE(n-1) 
     
def funcE(n):
    if n > 0:
        print("E:", n)
        funcA(n-1)                      
  
funcA(10)
