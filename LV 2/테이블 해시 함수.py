def solution(data, col, row_begin, row_end):
    S = []
    data.sort(key=lambda x:(x[col-1], -x[0]))

    for i in range(row_begin-1, row_end):
        modSum = 0
        for num in data[i]:
            modSum += num%(i+1)
        S.append(modSum)

    res = S[0]
    for i in range(1, len(S)):
        res = res ^ S[i] # XOR 연산

    return res

'''
* sort 함수, sorted함수에서의 key 사용법
1. key가 하나일 때
  1) 리스트의 각 원소를 기준으로 정렬
    ex) arr = ['abc', 'sdf', 'rtwe']
        arr.sort(key=lambda x:x) # 각 원소를 사전순으로 정렬
        print(arr) # 출력값: ['abc', 'rtwe', 'sdf']
  2) 리스트의 각 원소의 첫 글자를 기준으로 정렬
      ex) arr = ['abc', 'sdf', 'rtwe']
          arr.sort(key=lambda x:-x[0]) //첫번째 글자 기준으로 내림차순 정렬
          print(arr) # 출력값: ['sdf', 'rtwe', 'abc']
  3) 리스트 요소의 순위를 index로 정렬하는 방법 -> sorted함수 이용(반환값으로 새롭게 정렬된 리스트를 반환한다)
      ex) arr = [[1, 2], [6, 5], [5, 4], [5, 8], [7, 1], [10, 5]]
          sorted(range(len(arr)), key=lambda x: (arr[x][0], arr[x][1]), reverse = True) # 리스트의 각 요소에서 첫번째 요소(arr[x][0])를 기준으로 range(len(arr))를 내림차순 하고, 
                                                                                        # arr[x][0]이 같다면 두번째 요소 arr[x][1]기준으로 내림차순하여 정렬
                                                                                        # 1. 첫 번째 요소를 기준으로 내림차순을 진행 => [[1, 2], [6, 5], [5, 4], [5, 8], [7, 1], [10, 5]] 이므로, range의 순서는 5, 4, 1, (2, 3), 0이 된다.
                                                                                        #    첫 번째 요소가 5로 같기 때문에, 2번째와 3번째 값은 순위를 매길 수 없다 (편의상 (2, 3)로 표기)
                                                                                        # 2. 두 번째 요소를 기준으로 내림차순을 진행 => [5, 4], [5, 8] 중에서 [5, 8]이 더 크기 때문에, 더 높은 순위를 받게 된다.
                                                                                        # => 결과 : [5, 4, 1, 3, 2, 0]
          print(arr) # 출력값: [5, 4, 1, 3, 2, 0]

2. key가 여러개일때 lambda함수 사용하여 정렬 순서를 정할 수 있다.
ex) x[0]을 기준으로 오름차순 한 후에, 만약 x[0]값이 같다면 그 다음으로는 x[1]값 기준으로 내림차순(내림차순 할때는 -기호를 붙이면된다.)
    arr = [[1, 5], [6, 2], [6,4]]
    arr.sort(key=lambda x:(x[0], -x[1]))
    print(arr) # 출력값: [[1, 5], [6, 4], [6, 2]]
'''