def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

# print(twoSum(nums=[3, 2, 4], target=6))

def two_sum(nums, target):
    hashmap = {}
    for index, num in enumerate(nums):
        # print(index, num)
        print(hashmap)
        lookup = target - num
        if lookup in hashmap.keys():
            return hashmap[lookup], index
        else:
            hashmap[num] = index

# print(two_sum(nums=[3, 2, 4], target=6))