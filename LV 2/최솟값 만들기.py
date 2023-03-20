def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    res = 0
    for a, b in zip(A, B):
        res += a * b
    return res

'''
접근 방법
A배열의 원소와 B배열의 원소를 곱하고 더한 값의 최솟값을 구하는 문제(중복 사용x)
따라서, A배열은 오름차순으로, B배열은 내림차순으로 정렬하여 각 원소끼리 곱한 값을 더한 값이 최솟값이 된다.
'''