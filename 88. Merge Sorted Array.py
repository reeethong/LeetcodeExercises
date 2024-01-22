class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        removed_nums2 = 0
        removed_nums1 = 0 
        x = m+n
        pos = 0
        while pos < x:
            if nums1[pos] == 0 and removed_nums1 == m:
                del nums1[pos:]
                for i in range(len(nums2)):
                    nums1.append(nums2[i])
                pos = x
                break
            if removed_nums2 < n and nums1[pos] > nums2[0]:
                nums1.insert(pos,nums2[0])
                nums2.pop(0)
                removed_nums2 +=1
            else:
                removed_nums1 += 1
            pos +=1
        if len(nums1)> m+n:
            del nums1[m+n:]

                    
