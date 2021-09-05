
def LoopOver(num):    
    temp = Strobo_Num(num, num)
    return temp
      

def Strobo_Num(num, lent):
    if num == 0: return ['']
    if num == 1: return ['0','1','8']
    digits = Strobo_Num(num - 2, lent)
    temp = []
    for digit in digits:
        if num != lent:            
            temp.append("0" + digit + "0")
        temp.append('1' + digit + '1')
        temp.append('6' + digit + '9')
        temp.append('8' + digit + '8')
        temp.append('9' + digit + '6')
    return temp
  

if __name__ == '__main__':
    print(LoopOver(4))
