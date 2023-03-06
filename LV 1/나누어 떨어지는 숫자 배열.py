def solution(arr, divisor):
    answer = []
    for x in arr:
        if x % divisor == 0:
            answer.append(x)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)

''' 한줄 코드
def solution(arr, divisor): 
  return sorted([n for n in arr if n%divisor == 0]) or [-1]
'''