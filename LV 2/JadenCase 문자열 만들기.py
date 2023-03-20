def solution(s):
    strList = s.split(" ")
    res = []

    for x in strList:
        ch = ""
        if x == "":
            res.append("")
            continue
        if x[0].isalpha():
            ch = x[0].upper()
            if len(x) > 1:
                x = ch + x[1:].lower()
            else:
                x = ch
        else:
            x = x[0] + x[1:].lower()         
        res.append(x)

    return " ".join(res)


'''
split()함수의 사용법
1. split() -> 모든 공백문자(공백 1개건 공백 2개건 줄바꿈이건 간에 모든 공백문자) 기준으로 split
  ex) 문자열 사이의 공백이 2개가 있는 경우 -> s = "abc df     ers"인 경우
      s = s.split() -> s 결과: ["abc", "df", "ers"]

2. split('sep') 형태
  ex1) split(" ") -> 공백문자 1개 기준으로 split  
       문자열 사이의 공백이 2개가 있는 경우 -> s = "abc df  ers"인 경우 (df와 ers사이 공백2개)
       s = s.split() -> s 결과: ["abc", "df", "", "ers"]
  ex2) split(",") -> ","문자 기준으로 split

3. split(sep, count) 형태 -> sep은 구분자, count는 분할 횟수
'''