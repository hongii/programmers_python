def solution(storey):
    cnt = 0
    while storey > 0:
        # 일의자리 숫자 부터 판단
        num = storey % 10

        # 일의자리 숫자가 6 이상이거나, 일의자리 숫자가 5 이상이면서 그 앞의 자릿수(십의 자릿수)가 5이상인 경우 -> +버튼을 눌러서 층수를 올리는게 이득
        if num >= 6 or (num == 5 and (storey//10)%10 >= 5):
            cnt += 10 - num
            storey += 10 - num
        
        # 이외의 경우에는 -버튼을 누르는것이 이득
        else:
            cnt += num
        storey //= 10 

    return cnt

'''
* 참고한 풀이 힌트 *
올리면 무조건 이득보는 숫자는 6,7,8,9 이며, 내리면 무조건 이득보는 숫자는 0,1,2,3,4 입니다.
문제는 숫자 5입니다.
숫자 5일때 경우에 따라서 올리는게 더 좋을때가 있고, 오히려 내릴때 더 좋을때가 있습니다.

EX) 45 : 45인경우는 첫째자리 5를 내리는게 더 빨리 도착합니다 = 9번
5555: 첫째자리 5를 올리는게 더 빨리 도착합니다 = 18 5555> 5560->5600->6000->10000->0 : 5+4+4+4+1=18번
55: 55인 경우는 첫째자리를 올리든, 내리든 값이 똑같습니다 =10 55->60->100->0 :10 55->50->0: 10번
이렇게 숫자 5인 경우는 다양한 값이 나옵니다.

이 기준이 해당 자릿수의 다음 숫자가 5이상인가? 에서 판별이납니다.

45인 경우는 일의 자리가 5이고, 십의자리가 4(5보다작음)이므로, 내리는게 더 좋고,
5555인 경우는 일의자리가 5이고 십의자리가 5(5이상) 이므로, 올리는게 더 좋습니다.
'''


''' 처참하게 틀린 첫번째 풀이 -> 숫자 자릿수의 가장 앞부터 판단, 사실 주어진 테케 한정으로는 버튼 누르는 횟수만 판단하고 무슨 버튼을 누르는지는 구해도 되지 않으므로
-버튼을 먼저 눌러도 크게 상관은 없다만, 문제 조건에 0층 이하로 내려갈 수 없다고 했으므로 해당 풀이는 이상적인 풀이는 아님. -> 끼워 맞추기식 풀이..
즉, 내 코드대로라면 테케의 풀이와 다르게, 2554 -> -1000버튼 3번(=-3000): 3000-2556 = 446 -> -100버튼 4번: 46 -> -10버튼 5번: 10-6 = 4 -> +1버튼 4번... ㅋㅋ 
def solution(storey):
    cnt = 0
    while storey > 0:
        c = len(str(storey)) - 1
        cnt += storey // (10**c)
        storey = storey % (10**c)
        
        if 10**c - storey < (10**c) // 2:
            cnt += 1
            storey = 10**c - storey
    return cnt
'''