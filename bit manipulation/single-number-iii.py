# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor_of_nums = 0
        for num in nums:
            xor_of_nums = xor_of_nums ^ num
            
        index = 0
        xor_of_nums_copy = xor_of_nums
        
        #first bit which which is set in xor_of_sum, we find this because this is the bit which differs in both
        #the numbers.
        while True:
            if xor_of_nums_copy & 1:
                break
            index += 1
            xor_of_nums_copy = xor_of_nums_copy >> 1
        
        shift_val = 1 << index
        
        #finding xor of those numbers which has that bit set, which ultimately gives us one of the number.
        num1 = 0
        for num in nums:
            if num & shift_val:
                num1 = num1 ^ num
        
        return [num1, xor_of_nums ^ num1]