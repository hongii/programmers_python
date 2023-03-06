def solution(arr):
    if len(arr) == 1:
        return [-1] 
    arr.pop(arr.index(min(arr)))
    return arr

''' 참고
* pop()과 remove()함수의 차이 *
  pop() : 지정한 위치 값을 삭제하고 삭제한 값 취득
  remove() : 지정한 위치 값과 같은 값을 검색후 처음 값을 삭제

  따라서, 삭제한 값을 취득할 필요가 없다면
  arr.pop(arr.index(min(arr))) 보다는 arr.remove(min(arr))를 사용하는 것이 좋다.
  -> arr.remove(min(arr)) : 배열 arr에서 최소값을 찾아 그 값을 삭제한다.(문제 조건에서는 중복값이 없는 arr이므로 최소값은 하나이다.)
'''