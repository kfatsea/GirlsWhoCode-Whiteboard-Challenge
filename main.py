
MAX_LENGTH = 10**5
MAX_VALUE = 10**9

def repeatedValue(nums):
    if len(nums) > MAX_LENGTH:
        print("Array length exceeds maximum limit")
        return 2

    for i in range(len(nums)):
        if abs(nums[i]) > MAX_VALUE:
            print(f"Value {nums[i]} outside valid range")
            return 2

        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                print(f"Found duplicate: {nums[i]}")
                return 1

    print("No duplicates found")
    return 0

def optimizedRepeatedValue(nums):
    if len(nums) > MAX_LENGTH:
        print("Array length exceeds maximum limit")
        return 2
    
    seen = set()
    for num in nums: 
        if abs(num) > MAX_VALUE:
            print(f"Value {num} outside valid range")
            return 2
        if num in seen:
            print(f"Found duplicate: {num}")
            return 1
        seen.add(num)
    
    print("No duplicates found")
    return 0

nums = [-20, -1, 1, 3, 3, 4, 3, 2, 4, 2]
optimizedRepeatedValue(nums)
