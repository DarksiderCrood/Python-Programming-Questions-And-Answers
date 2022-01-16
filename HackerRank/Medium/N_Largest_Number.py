def checkAndPrint(n):
    # Write your code here
    l = [1,2,3,4,5,6,7,8,9,10]
    l.sort(reverse=True)
    print(l[n-1])

if __name__ == '__main__':
    n = int(input().strip())

    checkAndPrint(n)