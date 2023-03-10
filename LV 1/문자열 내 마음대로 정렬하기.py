def solution(strings, n):
    resSort = []
    for word in strings:
        resSort.append((word[n], word))
    resSort.sort()
    return [x[1] for x in resSort]

''' 최적의 풀이 : lambda 함수 이용
def solution(strings, n):
    strings.sort() # n=2인 경우, "abcd", "abce"에서는 비교할 값이 "c"로 동일하므로, 이때는 전체 문자열을 기준으로 사전순으로 정렬해야 한다. 
                    # 따라서 먼저 strings 배열을 사전순으로 정렬 한 후, 아래의 코드를 실행하면 제대로 정렬된다.
    return sorted(strings, key=lambda x: x[n])
'''