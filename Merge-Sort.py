
"""
Merge-sort function, any built-in or imported sorting functions or methods are not allowed.
"""
# Design:
# * A a way to split lists into to several parts and merge them
# * Comparison process, that sorts to their value
# * A Merging process

def order_switcher(list):
    """
    Functions reads input list from left to right.
    Compares current read value to next value and switches place if current is greater.
    Is intended to be used for lists of length 2
    Example: [1,2] -> [1,2] (no change), [2,1] -> [1,2] (ordered)
    :param list:
    :return list:
    """

    try:
        for x in range(len(list)):
            if list[x + 1] < list[x]:
                number_memory = list[x]
                list[x] = list[x + 1]
                list[x + 1] = number_memory
                print(list, x)
    except IndexError:
        pass

    return list

# List splitter, split list into pairs of two if even, if odd split, make last single list

slicednumber_list = []

list = [5,2,6,3]


while len(list) >= 1:
    slicednumber_list.append(order_switcher(list[:2]))
    for _ in range(2):
        list.pop(0)

print(slicednumber_list)

sorted_list = [1]
removal_flag = True
# del is bad
while sorted_list:
    if removal_flag:  # Clunky removal of list item to allow while-loop to run
        sorted_list.remove(1)
        removal_flag = False
    print(sorted_list, slicednumber_list)
    for lesser_list in range(len(slicednumber_list)):
        try:
            if not slicednumber_list[lesser_list][:]:  # if-block performs removal of empty lists
                sorted_list.append(slicednumber_list[lesser_list + 1][0])
                slicednumber_list.remove(slicednumber_list[lesser_list])
            elif not slicednumber_list[lesser_list + 1][:]:
                sorted_list.append(slicednumber_list[lesser_list][0])
                slicednumber_list.remove(slicednumber_list[lesser_list + 1])

            if slicednumber_list[lesser_list][0] < slicednumber_list[lesser_list + 1][0]:
                sorted_list.append(slicednumber_list[lesser_list][0])
                slicednumber_list[lesser_list].pop(0)
            else:
                sorted_list.append(slicednumber_list[lesser_list + 1][0])
                slicednumber_list[lesser_list + 1].pop(0)
                break
        except IndexError:
            pass

print(sorted_list)
