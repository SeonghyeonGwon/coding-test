from itertools import combinations
import math

def isPrimeNumber(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def solution(nums):
    count = 0
    
    for combination in list(combinations(nums, 3)):
        if isPrimeNumber(sum(combination)):
            count += 1
            
    return count