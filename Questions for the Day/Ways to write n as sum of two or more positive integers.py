def CountWays(num):
    output =[0] * (num + 1)
    output[0] = 1
    for x in range(1, num ):
        for y in range(x , num + 1):
            output[y] = output[y] + output[y - x]           
    return output[num]

 
if __name__ == '__main__':
    inp = int(input("Enter the numner: "))
    result = CountWays(inp)
    print(result)