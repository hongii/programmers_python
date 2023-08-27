''' 문제풀기 위해 필요한 캐시 알고리즘 지식
1. 캐시 알고리즘 - LRU 란?
=> LRU(Least Recently Used)는 가장 오랫동안 참조되지 않은 페이지를 교체하는 방식이다.
  LRU 는 사용된지 가장 오래된 페이지는 앞으로도 사용될 확률이 낮다는 가설에 의해 만들어진 알고리즘이다.

2. LRU 의 원리
=> LRU 를 구현하기 위해서는 캐시가 가득 찼을때, 가장 오랫동안 참조되지 않은 페이지를 찾아서 없애는 과정이 필요하다.
  페이지를 새로 참조할 때마다 연결리스트의 맨 앞에 페이지번호를 추가한다.
  그러면 맨 뒤에 있는 페이지번호가 가장 오랫동안 참조되지 않은 페이지번호가 된다.
  따라서 LRU의 원리는, 캐시의 크기가 3인데 이미 3개의 페이지가 캐시에 들어있다면 맨 뒤에 있는 페이지번호 node를 지우고 새로운 페이지번호 node를 앞에 연결해주는 방식이다.
  LRU를 구현할때는 Doubly Linked List를 사용하고 head에 가까운 node일수록 가장 최근에 참조된 페이지, tail에 가까운 node일수록 가장 오랫동안 참조되지 않는 페이지이다. 
  LRU 의 개념에 따라 cache size를 넘어서게 된다면 tail 에 가까운 페이지가 먼저 삭제되도록 한다. 
  => cache miss : CPU 가 참조하고자 하는 메모리(참조값)가 캐시에 존재하지 않을 경우 -> head에 해당 참조값을 추가한다.
  => cache hit : CPU 가 참조하고자 하는 메모리(참조값)가 캐시에 존재하고 있을 경우 -> 해당 참조값을 캐시의 head 위치로 옮긴다.
'''

# 2회차 코드
from collections import deque
def solution(cacheSize, cities):
    hit, miss = 1, 5
    if cacheSize ==  0:
        return len(cities) * miss
    
    cache = deque()    
    times = 0
    for city in cities:
        city = city.lower()
        if city not in cache:
            times += miss
            if len(cache) == cacheSize:
                cache.pop()
            cache.appendleft(city)
        else:
            times += hit
            cache.remove(city)
            cache.appendleft(city)
    return times


# 1회차 코드
from collections import deque
def solution(cacheSize, cities):
    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    cache = deque()
    time = 0
    for city in cities:
        if city not in cache:
            time += 5
            if len(cache) >= cacheSize and cacheSize > 0:
                cache.pop()
            elif cacheSize == 0:
                continue
            cache.appendleft(city)

        else:
            cache.remove(city)
            cache.appendleft(city)
            time += 1
    return time