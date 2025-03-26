def solution(players, m, k):
    answer = 0
    servers = [0] * (len(players) + k)  # i: 서버 반납 시간, servers[i]: i시간에 반납할 서버 갯수를 저장
    now_max = m-1  # 현재 수용가능한 최대 인원 -> m명 미만일 경우 서버 증설 필요 x, 초기 처리 가능한 인원은 m-1

    for i, p in enumerate(players):
        now_max -= servers[i] * m  # 현재 시간(i)에 반납되어야 할 서버 처리
        if now_max < p:  # 서버가 부족한 경우
            add_servers = (p - now_max + m - 1) // m # 필요한 서버 개수
            answer += add_servers
            now_max += add_servers * m  # 추가된 서버 증설 수 반영
            servers[i + k] += add_servers  # k 시간 지난 후에 반납해야 할 서버 갯수 저장(지금 증설된 서버 수)

    return answer