def solution(sequence):
  minus_plus = [] # [-1, 1] 펄스수열 곱한 배열
  plus_minus = [] # [1, -1] 펄스수열 곱한 배열
  for i in range(1, len(sequence)+1): 
    if i % 2 == 0:
        minus_plus.append(sequence[i-1])
        plus_minus.append(sequence[i-1]*-1)
    else:
        minus_plus.append(sequence[i-1]*-1)
        plus_minus.append(sequence[i-1])

  dp_mp = [0]*(len(sequence)) # minus_plus배열의 최대 부분합 저장
  dp_pm = [0]*(len(sequence)) # plus_minus배열의 최대 부분합 저장
  for i in range(len(sequence)): # 연속 수열의 최대 부분합 구하기
      dp_mp[i] = max(0, dp_mp[i-1]) + minus_plus[i]
      dp_pm[i] = max(0, dp_pm[i-1]) + plus_minus[i]

  return max(max(dp_mp), max(dp_pm))


'''
# 다른 사람의 풀이 -> sequence[i] * (-1) ** i를 통해 새로운 배열을 만듦. 
def solution(sequence):
  answer = 0
  n = len(sequence)

  dp1 = [sequence[i] * (-1) ** i for i in range(n)] 
  dp2 = [sequence[i] * (-1) ** (i + 1) for i in range(n)]
  seq1 = [sequence[i] * (-1) ** i for i in range(n)]
  seq2 = [sequence[i] * (-1) ** (i + 1) for i in range(n)]

  for i in range(n): 
    if i >= 1:
      dp1[i] = max(dp1[i - 1] + seq1[i], seq1[i])
      dp2[i] = max(dp2[i - 1] + seq2[i], seq2[i])

  return max(max(dp1),max(dp2))
'''