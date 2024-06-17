def solution(A: list[int], R: int):
    if R == len(A):
        return 0

    count = {}
    num_distincts = 0
    for i in range(R, len(A)):
        if A[i] not in count:
            num_distincts += 1
            count[A[i]] = 1
        else:
            count[A[i]] += 1

    result = num_distincts
    for i in range(len(A) - R + 1):
        start = i
        end = i + R
        if end < len(A):
            count[A[end]] -= 1
            if count[A[end]] == 0:
                num_distincts -= 1

            if A[start] not in count:
                count[A[start]] = 1
                num_distincts += 1
            else:
                count[A[start]] += 1
                if count[A[start]] == 1:
                    num_distincts += 1
            result = max(result, num_distincts)

    return result


if __name__ == "__main__":
    A = [2, 1, 2, 3, 2, 2]
    R = 3
    print(solution(A, R))
    A = [2, 3, 1, 1, 2]
    R = 2
    print(solution(A, R))
    A = [20, 10, 10, 10, 30, 20]
    R = 3
    print(solution(A, R))
    A = [1, 100000, 1]
    R = 3
    print(solution(A, R))
