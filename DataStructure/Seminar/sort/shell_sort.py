def insertion_sort(list, start, gap):
    for i in range(start+gap, len(list), gap):

        key = list[i]
        index = i

        while index >= gap and list[index-gap] > key:
            list[index] = list[index - gap]
            index -= gap

        list[index] = key

def shell_sort(list):
    gap = len(list)//2

    while gap > 0:

        for start in range(gap):
            insertion_sort(list, start, gap)

        print("list : ", list)

        gap //= 2


list = [8, 5, 6, 2, 4, 11, 10, 9, 7]

shell_sort(list)

print(list)
