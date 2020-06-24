from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if target >= nums[0] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

        


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([1], 1))
    print(s.search([3, 1], 1))