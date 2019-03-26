def selection_sort(list):
    for i in range(len(list) - 1):

        least = list.index(min(list[i:]))

        if i != least:
            list[i], list[least] = list[least], list[i]


list = [9, 6, 7, 3, 5, 10, 11, 17, 12, 13]

selection_sort(list)
print(list)
