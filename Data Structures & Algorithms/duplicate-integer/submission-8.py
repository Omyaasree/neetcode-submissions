class Solution:
    from collections import defaultdict
    def hasDuplicate(self, nums: List[int]) -> bool:
        valid = False

        hashmap = {}
        for i in nums:
            if i in hashmap:
                return True
            else :
                hashmap[i] = 1
        
        return False