# 다른 사람 풀이 참고
def solution(numbers):
    ans = []
    for num in numbers:
        cnt = 0 # 마지막 자릿수부터 연속된 1의 갯수 
        bNum = bin(num)[2:]
        for n in bNum[::-1]:
            if n == "1":
                cnt += 1
            else:
                break

        # 짝수인 경우 cnt = 0이므로, 최소 1을 더해주기 위함 
        # ex. 짝수는 이진수로 바꾸면 항상 0으로 끝나므로, 마지막 자리의 연속된 1의 갯수는 0개 이다.
        # 이 경우, 2**(cnt-1) = 2**(0-1) = 0.5 가 되므로, cnt = 1로 바꾸어 계산해주면 된다.
        # 짝수의 경우(ex. num=8)에는 그 값에서 +1 해준 값이 최소 비트 2개 이하로 차이나므로 결과값 res = 8 + (2**(1-1)) = 8 + 1 = 9가 된다.
        if cnt == 0: 
            cnt = 1
        res = num + (2**(cnt-1))
        ans.append(res)
    return ans

''' 테케 10번 11번 -> 시간초과
def solution(numbers):
    ans = []
    for num in numbers:
        n = num + 1
        
        while True:
            xorInt = num ^ n # xor연산은 서로 다른 비트일때 1, 서로 같을때 0
            xorBin = bin(xorInt)[2:]
            if xorBin.count("1") <= 2:
                ans.append(n)
                break
            else:
                n += 1
    return ans
'''