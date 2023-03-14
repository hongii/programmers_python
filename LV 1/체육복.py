def solution(n, lost, reserve):
    check = [0]*(n+1)
    saveCnt = 0

    # 여분 체육복을 가져온 학생이 체육복도 잃어버린 경우 -> 그냥 체육복 하나만 있는 학생으로 취급
    # ex) lost=[2,3], reserve=[3,4]인 경우, 3번 학생은 그냥 두 배열에서 제거한다.
    intersection = list(set(lost) & set(reserve))
    for i in range(len(intersection)):
        lost.remove(intersection[i])
        reserve.remove(intersection[i])

    # 여분 체육복이 있는 학생 check
    for i in range(len(reserve)):
        check[reserve[i]] = 1

    # lost 리스트가 오름차순으로 정렬되어 있어야 여분 체육복을 가진 학생들 중 가장 앞번호인 학생으로 부터 체육복을 받을 수 있다. 
    # ex) lost=[4, 2], reverse=[3, 5]인 경우, 4번 학생이 3번으로 부터 체육복을 빌려가면 2번 학생은 체육복을 빌리지 못하는 경우가 발생한다.
    #     따라서, 오름차순 정렬을 하여 2번학생이 3번 학생한테 체육복을 빌리고, 4번 학생이 5번 학생한테 체육복을 빌리도록 해야한다.
    lost.sort() 
    
    for i in range(len(lost)):
        if lost[i] != 1 and check[lost[i]-1] == 1:
            check[lost[i]-1] = 0 
            saveCnt += 1
        elif lost[i] != n and check[lost[i]+1] == 1:
            check[lost[i]+1] = 0
            saveCnt += 1

    return n - len(lost) + saveCnt