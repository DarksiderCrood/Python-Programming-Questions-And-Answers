'''
Aahad and Harshit always have fun by solving
problems. Harshit took a sorted array and rotated it
clockwise by an unknown amount. For example,
he took a sorted array = [1, 2, 3, 4, 5] and if he rotates
it by 2, then the array becomes: [4, 5, 1, 2, 3].
After rotating a sorted array, Aahad needs to answer

Q queries asked by Harshit, each of them is described
by one integer Qi] which Harshit wanted him to search
in the array. For each query, if he found it,
he had to shout the index of the number, otherwise,
he had to shout -1.

Note:
You are not required to explicitly print the expected
output, just return it and printing has
already been taken care of.
'''
def solution(arr, q) :
    
    start = 0
    end = len(arr) - 1
    while(start <= end) :

        mid = start + (end - start) // 2
        
        if(arr[mid] == q) :
            return mid
        
        elif(arr[mid] >= arr[start]) :

            if(arr[start] <= q and q <= arr[mid]):
                end = mid - 1
            else :
                start = mid + 1
            
        else :
            if(arr[end] >= q and q >= arr[mid]) :
                start = mid + 1
            else :
                end = mid - 1

    return -1
