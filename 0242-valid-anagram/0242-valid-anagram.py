class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are not the same, return False immediately
        if len(s) != len(t):
            return False

        # Convert strings to lists of characters
        s_list = list(s)
        t_list = list(t)
        
        # Perform merge sort on both lists
        self.mergeSort(s_list, 0, len(s_list) - 1)
        self.mergeSort(t_list, 0, len(t_list) - 1)
        
        # Compare the sorted lists
        return s_list == t_list

    # Merge Sort Function
    def mergeSort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            
            # Recursively divide the array
            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)
            
            # Merge the two halves
            self.merge(arr, left, mid, right)

    # Merge Function to combine sorted halves
    def merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        
        # Temporary arrays for merging
        left_half = [0] * n1
        right_half = [0] * n2
        
        # Copy data to temporary arrays
        for i in range(n1):
            left_half[i] = arr[left + i]
        
        for j in range(n2):
            right_half[j] = arr[mid + 1 + j]
        
        # Merge the temporary arrays back into arr
        i = 0  # Index for left_half
        j = 0  # Index for right_half
        k = left  # Index for arr
        
        while i < n1 and j < n2:
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Copy remaining elements of left_half if any
        while i < n1:
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Copy remaining elements of right_half if any
        while j < n2:
            arr[k] = right_half[j]
            j += 1
            k += 1