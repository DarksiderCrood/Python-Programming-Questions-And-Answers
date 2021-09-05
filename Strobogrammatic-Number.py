
def LoopOver(n):
      
    temp = Strobo_Num(n, n)
    return temp
      

def Strobo_Num(n, length):
      
    if n == 0: return [""]
    if n == 1: return ["1", "0", "8"]
      
    middles = Strobo_Num(n - 2, length)
    temp = []
      
    for middle in middles:
        if n != length:            
            temp.append("0" + middle + "0")
  
        temp.append("8" + middle + "8")
        temp.append("1" + middle + "1")
        temp.append("9" + middle + "6")
        temp.append("6" + middle + "9")
    return temp
  

if __name__ == '__main__':
    print(LoopOver(4))
