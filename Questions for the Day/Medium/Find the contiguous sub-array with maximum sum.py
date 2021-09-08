'''
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Example 1:
Input:
    N = 5
    arr[] = {1,2,3,-2,5}
Output:
    9
Explanation:
    Max subarray sum is 9
    of elements (1, 2, 3, -2, 5) which 
    is a contiguous subarray.

Example 2:
Input:
    N = 4
    arr[] = {-1,-2,-3,-4}
Output:
    -1
Explanation:
    Max subarray sum is -1 
    of element (-1) 
Time Complexity must be: 
    O(N)
Constraints: 
    1 ≤ N ≤ 10^6
'''

# Method 1
def max_sum(arr, lenght):     
    first_max =arr[0]
    present_max = arr[0]
    for i in range(1,lenght):
        present_max = max(arr[i], present_max + arr[i])
        first_max = max(first_max,present_max)   
    return first_max


if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print("The contiguous sub-array with maximum sum: {}".format(max_sum(arr,len(arr))))


# Method 2
# Using Kadane’s Algorithm
class MaxSub:
    def SubArrayWithMaxSum(arr):
        first_max = arr[0]
        present_max = arr[0]
        for i in range(1, len(arr)):
            first_max = first_max+arr[i]
            if first_max<arr[i]:
                first_max=arr[i]
            if present_max < first_max:
                present_max = first_max
        return present_max

arr = [-1,-2,-3,-4,0]
obj = MaxSub
result = obj.SubArrayWithMaxSum(arr)
print("The contiguous sub-array with maximum sum: {}".format(result))