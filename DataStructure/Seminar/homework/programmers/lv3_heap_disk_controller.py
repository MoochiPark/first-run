import heapq

l = [[0, 3], [1, 9], [2, 6]]


def solution(jobs):
    heapq.heapify(jobs)
    time = 0
    time_sum = 0
    processed = 0
    heap = []
    while jobs:
        request_time, process = heapq.heappop(jobs)

        if processed == 0:
            time_sum = process
        else:
            time_sum += time - request_time + process

        if processed == 0:
            time = request_time + process
        else:
            time += process

        processed += 1

        while jobs and jobs[0][0] < time:
            request_time, process = heapq.heappop(jobs)
            heapq.heappush(heap, [-process, request_time])
            print("#",heap)
        while heap:
            process, request_time = heapq.heappop(heap)
            jobs.insert(0, [request_time, -process])

    return time_sum // processed


print(solution(l))
