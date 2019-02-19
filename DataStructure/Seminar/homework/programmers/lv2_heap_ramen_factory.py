import heapq

st = 4
da = [4, 10, 15]
sup = [20, 5, 10]
k = 30


def solution(stock, dates, supplies, k):
    answer = 0
    n = 0
    heap = []

    while stock < k:
        for i in range(n, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(heap, supplies[i])
            else:
                n = i
                break
        heapq._heapify_max(heap)
        stock += heapq.heappop(heap)
        answer += 1
    return answer


print(solution(st, da, sup, k))
