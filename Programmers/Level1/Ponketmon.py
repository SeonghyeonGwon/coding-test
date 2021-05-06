def solution(nums):
    data = set(nums)
    
    if len(data) > len(nums) / 2:
        return len(nums) / 2
    else:
        return len(data)