'''
Bubble sort
Time: O(n^2)
space: o(1)
'''

def bubble_sort(lst):
    count_outer = 0
    count_inner = 0

    for i in range(len(lst)):
        count_outer +=1
        swapped = False

        for j in range(len(lst) - i - 1):
            count_inner+=1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True

        if not swapped:
            break

    print(f'outer {count_outer}, inner {count_inner}')
    return lst

# print(bubble_sort([1, 2, 5, 50, 90]))
print(bubble_sort(['colt','bull', 'poco', 'gale']))

'''
inner for loop
j = 5
01, 12, 23, 34, 4'5'-> error 

j = 4
01, 12, 23, 34
'''
