hei = [2, 2, 2, 2, 2, 2, 5]


def solution(heights):
    answer = []
    for i in range(1, len(heights)):

        for j in range(i, 0, -1):
            if heights[i] < heights[j - 1]:
                answer.append(j)
                break
            elif heights[i] >= heights[j - 1] and j == 1:
                answer.append(0)
            else:
                continue

    return [0] + answer


print(solution(hei))
