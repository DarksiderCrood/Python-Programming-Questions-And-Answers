
def LoopOver(n):    
    temp = Strobo_Num(n, n)
    return temp
      

def Strobo_Num(n, lent):
    if n == 0: return [""]
    if n == 1: return ["1", "0", "8"]
      
    digits = Strobo_Num(n - 2, lent)
    temp = []
      
    for digit in digits:
        if n != lent:            
            temp.append("0" + digit + "0")
        temp.append("8" + digit + "8")
        temp.append("1" + digit + "1")
        temp.append("9" + digit + "6")
        temp.append("6" + digit + "9")
    return temp
  

if __name__ == '__main__':
    print(LoopOver(4))
