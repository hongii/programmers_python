# 다른사람 풀이 참고 
def solution(phone_book):
    res = True
    phone_book.sort() # 문자열(사전순) 오름차순 정렬
    for i in range(len(phone_book)-1):
        # 사전순으로 정렬했기 떄문에 다로 다음에 위치하는 원소랑 비교하면 된다. 
          # 하나라도 일치하는 접두어가 존재하기만 한다면 조건 성립이므로 다음 원소 비교할 필요 없음
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: 
            res = False
            break
    return res