
class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:

        """
        #Utilizes greedy checking
        to check if we can rob "k" houses with current maximum value.
        """
        def can_rob(maximum):
            counter = 0
            i = 0
            while i < len(nums):
                if nums[i] <= maximum:
                    counter += 1
                    i += 2
                    if counter == k:
                        return True
                else:
                    i += 1
            return False

        """
        #Utilizes binary search to look for the least
        maximum value that we can rob
        """
        low, high = min(nums), max(nums)
        result = high
        while low <= high:
            mid = (low + high) // 2
            if can_rob(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result





sol = Solution()
items_test =  (([24,109,117,142,98,94,91,130,73,48,107,77],5,98),
                ([2,7,9,3,1], 2, 2),
                ([2,3,5,9], 2, 5),
               ([4,22,11,14,25], 3, 25)
               )

for i in items_test:
    print(i[0],i[1])
    results = sol.minCapability(i[0], i[1])
    print("Expected: ",i[2])
    print("Actual: ",results)

