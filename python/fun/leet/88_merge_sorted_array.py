class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_index = m - 1
        right_index = n - 1
        insert_index = m + n - 1

        while right_index >=0:
            if left_index >= 0 and nums1[left_index] > nums2[right_index]:
                nums1[insert_index] = nums1[left_index]
                left_index -= 1
            else:
                nums1[insert_index] = nums2[right_index]
                right_index -= 1
            insert_index -= 1