# sort the array
import math 

def pallindum(nums):
     
    large = max(nums)
    big = []
    countB = 1
    
    
    for i in range(len(nums)):
        if large == nums[i]:
            countB +=1
            total = nums[i] * countB 
            print(total)
            
   


pallindum([3,1,4,4])    