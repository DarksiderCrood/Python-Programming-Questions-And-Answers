def pascal_triangle(arr, n):
   row = [1]
   y = [0]
   arrstr = ''.join(str(k) for k in arr)
   iarrl = len(arr)
   for _ in range(max(n,0)):
      print(row) # print pascal triangle till nth rows
      rowstr = ''.join(str(k) for k in row)
      if arrstr in rowstr:
          print(row[iarrl])
      row=[l+r for l,r in zip(row+y, y+row)]
   return n>=1


if __name__ == '__main__':
    arr = [1,5] 
    n = max(arr)+1
    pascal_triangle(arr, n) 

