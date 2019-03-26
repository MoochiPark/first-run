def insertion_sort(list):
    for index in range(1, len(list)):
        while 0 < index and list[index] < list[index - 1]:
            list[index], list[index - 1] = list[index - 1], list[index]
            index -= 1


list = [8, 5, 6, 2, 4]

insertion_sort(list)

print(list)
