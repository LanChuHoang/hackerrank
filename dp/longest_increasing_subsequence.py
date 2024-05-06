# competitive programming handbook

# find the longest increasing sub sequence in a given array

# bottom-up: O(n^2)
# idea: len(k) is the max len that end at index k
# len(k) = len(i) + 1 where
# i < k and arr[i] < arr[k]
# len(i) is largest


def o_squared_lis(arr: list[int]):
    max_so_far = 1
    max_len = [1] * len(arr)
    for k in range(1, len(arr)):
        for i in range(0, k):
            if arr[i] < arr[k]:
                max_len[k] = max(max_len[k], max_len[i] + 1)
        max_so_far = max(max_so_far, max_len[k])
    return max_so_far


if __name__ == "__main__":
    print(o_squared_lis([6, 2, 5, 1, 7, 4, 8, 3]))

    def lengthOfLIS(nums):
        # Binary search approach
        n = len(nums)
        ans = []

        # Initialize the answer list with the
        # first element of nums
        ans.append(nums[0])

        for i in range(1, n):
            if nums[i] > ans[-1]:
                # If the current number is greater
                # than the last element of the answer
                # list, it means we have found a
                # longer increasing subsequence.
                # Hence, we append the current number
                # to the answer list.
                ans.append(nums[i])
            else:
                # If the current number is not
                # greater than the last element of
                # the answer list, we perform
                # a binary search to find the smallest
                # element in the answer list that
                # is greater than or equal to the
                # current number.
                low = 0
                high = len(ans) - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if ans[mid] < nums[i]:
                        low = mid + 1
                    else:
                        high = mid
                # We update the element at the
                # found position with the current number.
                # By doing this, we are maintaining
                # a sorted order in the answer list.
                ans[low] = nums[i]

        # The length of the answer list
        # represents the length of the
        # longest increasing subsequence.
        return ans

    # Driver program to test above function
    nums = [6, 2, 5, 1, 7, 4, 8, 3]
    # Function call
    print("Length of LIS is", lengthOfLIS(nums))
