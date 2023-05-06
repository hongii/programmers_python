# 다른사람 풀이 참고 -> onBridge = deque([0]*bridge_length) : 다리길이 만큼의 배열을 먼저 생성하고 1초마다 맨 앞의 값을 제거한다.(1초마다 트럭이 한칸씩 이동하므로)
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    weigthSum = 0
    onBridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)

    while truck_weights:
        weigthSum -= onBridge.popleft()
        time += 1
        if weigthSum+truck_weights[0] <= weight:
            weigthSum += truck_weights[0]
            onBridge.append(truck_weights.popleft())
        else:
            onBridge.append(0) # 트럭이 다리 무게 제한 때문에 다리위로 트럭이 올라가지 못한경우, 0을 추가
        
    return time + bridge_length