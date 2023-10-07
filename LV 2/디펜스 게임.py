# 2회차 코드
import heapq as hq
def solution(n, k, enemy):
    if len(enemy) == k:
        return len(enemy)
    
    r = 0 # 라운드 횟수
    soldier = [] # 무적권으로 처치한 적군을 담는 최소힙 -> 무적권 다쓰고나면, 무적권으로 처치한 적군의 수 중 가장 적은 수를 꺼내서 n(남은병사)에서 뺴주기 위함
    for i in range(len(enemy)):
        if k > 0: # 무적권 먼저 다씀
            k -= 1
            hq.heappush(soldier, enemy[i])
        else: 
            # 무적권 다쓰고 나면, 무적권으로 패스시킨 적군의 숫자 중 가장 작은 숫자(soldier[0])를 현재 처치할 적군의 수(enemy[i])와 비교
            if soldier[0] < enemy[i] and  n - soldier[0] >= 0: # 현재 처치할 적군의 수가 더 많다면, 무적권으로 패스시킨 적군과 바꿔치기
                n -= hq.heappop(soldier)
                hq.heappush(soldier, enemy[i])
            elif n - enemy[i] >= 0: # 무적권으로 패스시킨 적군의 수보다 현재 처치할 적군의 수가 더 적거나 같은 경우, 남아있는 병사들에서 현재 처치할 적군을 빼줌
                n -= enemy[i]
            else: # 남아있는 병사들의 수가 현재 처치할 적군의 수보다 더 적은 경우 -> 게임 종료
                break
        r += 1
    return r     


# 1회차 코드
import heapq as hq
def solution(n, k, enemy):
    if len(enemy) == k:
        return len(enemy)
    
    r = 0
    soldier = [] # 통과한 라운드에 사용된 병사의 수를 담는 최대힙
    for i in range(len(enemy)):
        # 가지고 있는 병사를 사용하여 라운드 통과하는 경우
        if n >= enemy[i]:
            n -= enemy[i]
            hq.heappush(soldier, -enemy[i]) 
            r += 1
            
        # 병사의 수가 모자른 경우 
        else:
            # 남은 무적권의 갯수가 1개 이상인 경우에만 추가 라운드 진행 가능
            if k > 0:
                # 현재 라운드의 적의 수보다 최대힙의 top에 위치한 병사의 수가 더 많은 경우 -> 해당 라운드에 사용된 병사의 수 만큼 도로 가져와서 현재 병사의 수에 더한다. 
                # 그리고 이미 통과한 라운드에 무적권을 사용하는 것으로 변경(롤백)
                if soldier and -soldier[0] > enemy[i]:
                    n += -hq.heappop(soldier)
                    n -= enemy[i]
                    hq.heappush(soldier, -enemy[i]) # 해당 라운드에 사용된 병사 수를 최대힙에 넣어줌
                
                # 최대힙이 비었거나 현재 라운드의 적의 수가 최대힙의 top에 위치한 병사의 수 이하라면, 그냥 현재 라운드에 무적권을 사용
                else: 
                    pass
                
                k -= 1
                r += 1
                
            else:
                break
                
    return r       



'''
* 참고한 아이디어 -> 최대힙 이용 : 지나온 라운드와 현재 라운드 중에서 가장 병사의 수가 많은 라운드에 무적권을 적용하는 방식
1. 우선 적의 수를 순서대로 우선순위 큐에 저장한다. 
2. 그리고 만약 병사의 수(n)가 0보다 적으면 무적권을 사용한다.
3. 이 때, 무적권은 우선순위 큐에 저장된 적의 수 중에서 가장 큰 값에 대해서 사용한다. 
-> 즉, 이미 병사의 수를 차감하여 라운드를 통과하였지만 다시 롤백하여 우선순위 큐의 가장 top에 위치한 값(사용한 병사의 수)만큼 다시 가져오고 
  해당 라운드(이미 지나온)에는 무적권을 사용하는 방식. 
  이 때 추가적으로 생각해야 할 부분은, 만약 현재 라운드의 적의 수(enemy[i])보다 최대힙의 top에 위치한 병사의 수가 더 적다면 그냥 현재 라운드에 무적권을 적용하고 넘어간다.
'''

''' 첫번째 코드 -> 40.6점... 이런식으로 경우의수 파악하는건 불가능하다고 판단 -> 풀이 참고하여 힙큐를 사용하는 코드로 수정
def solution(n, k, enemy):
    if len(enemy) == k:
        return len(enemy)
    
    r, m = 0, n
    for i in range(len(enemy)):
        if m >= enemy[i]:
            m -= enemy[i]
            r += 1
        else:
            if k > 0:
                k -= 1
                r += 1  
            else: 
                break
    return r            
'''