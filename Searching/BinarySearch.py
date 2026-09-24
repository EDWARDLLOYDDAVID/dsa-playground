# Binary Search
#
# Binary search finds a target value by repeatedly checking the middle element
# of a sorted sequence. If the middle value is smaller than the target, the
# left half is discarded. Otherwise, the right half is discarded.
#
# This method makes a copy of the input and sorts it before searching. The
# returned index therefore belongs to the sorted copy, not necessarily to the
# original list. Sorting first allows the method to accept an unsorted list.
#
# Supported data types:
# - Integers and floats: [1, 3, 5, 7]
# - Strings: ["apple", "banana", "mango"]
# - Booleans: [False, False, True, True]
# - Lists or tuples containing comparable values
#
# Dictionaries and sets are not searched directly as a whole. A dictionary can
# be searched through sorted keys, values, or items, and a set can be converted
# to a sorted list first. All values must be comparable with <, ==, and >.
#
# Time complexity for binary search after the data is sorted:
# - Best case: O(1), when the target is the first middle element checked
# - Average case: O(log n)
# - Worst case: O(log n), when the target is near the end of the search
#   or is not present
#
# Because this implementation sorts a copy first, the complete operation is:
# - Best case: O(n log n) because sorting is always performed
# - Average case: O(n log n)
# - Worst case: O(n log n)
#
# Space complexity:
# - O(n), because a copy of the input list is created
# - The binary search loop itself uses O(1) extra space

class BinarySearch(object):

    def __init__(self):
        pass

    def  search_binary(self, list, n):
        # Copy the input so the original list is not modified.
        data = list.copy()

        # Binary search requires sorted data. Sorting also allows unsorted input.
        data.sort()

        low = 0
        up = len(data)-1

        # Continue while there is still a valid search range.
        while low <= up:
            # Check the middle position of the current range.
            mid = (low + up)//2

            if (data[mid] == n):
                # Return the position in the sorted copy.
                return mid
            else:
                if (data[mid] < n):
                    # The target must be in the right half.
                    low = mid + 1
                else:
                    # The target must be in the left half.
                    up = mid - 1

        # -1 indicates that the target was not found.
        return -1

    
X = [1,5,9,6,7,3,5,9]

search = BinarySearch()

result = search.search_binary(X, 5)

result2 = search.search_binary(X, 10)

print(f"Found at index: {result}" if result >= 0 else "Element Not Found")
print(f"Found at index: {result2}" if result2 >= 0 else "Element Not Found")