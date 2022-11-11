array=[12,3,4,6,33,90,88,7]



# bubble sort (small to big)

# selection sort (big to small)
def sort(nums):
    for i in range(len(nums)):
        for j in range( len(nums)-1):
            if(nums[j]>nums[j+1]):
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
    return nums

print(sort(array))



# insertion sort
def insertion(num):
    for i in range(len(num)-1):
        minpos=num[i+1]
    

        while i>=0 and num[i]>minpos:
            num[i+1]=num[i]
            i-=1
            
        num[i+1]=minpos

    return num

print(insertion(array))



