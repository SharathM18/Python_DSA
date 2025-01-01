'''
Binary Search: Fast search in sorted arrays
Time: O(log n)
Space: O(1)

For strings, comparisons are case-sensitive. "Apple" is not equal to "apple"
print("Apple" < "apple")  # Output: True ('A' has a smaller Unicode value than 'a')
print("abc" < "abcd")  # Output: True
'''

def binary_search(lst, target):
    lower = 0
    upper = len(lst) - 1

    while lower <= upper:
        mid = (lower + upper) // 2

        if lst[mid] == target:
            return mid
        else:
            if lst[mid] < target:
                lower = mid + 1
            else:
                upper = mid - 1
    return -1

# res = binary_search([4, 7, 8, 12, 45, 99], 100)

res = binary_search(sorted(['bull', 'poco', 'brock', 'colt']), 'brock')

if res != -1:
    print(f'element found at index {res}')
else:
    print('element not found')



