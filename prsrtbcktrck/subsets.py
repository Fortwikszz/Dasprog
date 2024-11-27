nums = [1,2,3]
com = []

def find(com, nums, count, temp):
    com.append(temp)
    for i in range(count, len(nums)):
        find(com, nums, i+1, temp + [nums[i]])
        
    return com

com = find(com, nums, 0, [])

print(com)