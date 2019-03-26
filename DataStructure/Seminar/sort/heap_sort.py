import heapq

def heap_sort(list):
    n = len(list)

    for i in range(n // 2 - 1, -1, -1):
        heapq.heapify(list)
        for i in range(n - 1, 0, -1):
            list[0], list[i] = list[i], list[0]
            heapq.heapify(list)

list = [16, 14, 10, 4, 7, 9, 3, 2, 1]

heap_sort(list)

print(list)
