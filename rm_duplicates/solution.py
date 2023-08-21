def rm_duplicates(nums):
    hash = set()
    for num in nums:
        if num not in hash:
            hash.add(num)

    k = len(hash)
    return k
            

print(rm_duplicates(nums=[1,1,2]))
