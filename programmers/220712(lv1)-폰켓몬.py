nums1 = [3,1,2,3]
r1 = 2

nums2 = [3,3,3,2,2,4]
r2 = 3

nums3 = [3,3,3,2,2,2]
r3 = 2

def solution(nums):
    if len(nums) / 2 > len(set(nums)):
        return int(len(set(nums)))
    elif len(nums) / 2 < len(set(nums)):
        return int(len(nums) / 2)
    elif len(nums) / 2 == len(set(nums)):
        return int(len(nums) / 2)

print(f"{solution(nums1)} -> {r1}")
print(f"{solution(nums2)} -> {r2}")
print(f"{solution(nums3)} -> {r3}")