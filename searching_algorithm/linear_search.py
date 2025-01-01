'''
Linear Search/ Sequential Search
time complexity: o(n)
space complexity: o(1)
'''

def linear_search(lst, searched_ele):
    for i in range(len(lst)):
        if lst[i] == searched_ele:
            return i
    return -1

res = linear_search([10, 20, 50, 30, 100, 20], 20)

if res == -1:
    print(f'element not found ')
else:
    print(f'element found at index {res}')