pro = [5, 30, 17, 18, 23]

spe = [29, 21, 16, 12, 2]


def solution(progresses, speeds):
    answer = []

    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses:
            if progresses[0] >= 100:
                del progresses[0]
                del speeds[0]
                cnt += 1
                if progresses and progresses[0] >= 100:
                    continue
                else:
                    answer.append(cnt)
            else:
                break
    return answer


print(solution(pro, spe))
