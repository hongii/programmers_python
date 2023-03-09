def solution(s):
    words = s.split(" ")
    word = ""
    for x in words:
        for i in range(len(x)):
            if i % 2 == 0:
                word += x[i].upper()
            else:
                word += x[i].lower() 
        word += " "
    return word[:-1]

'''
테케 오류 -> 힌트 모음집 참고 : https://school.programmers.co.kr/learn/courses/14743/lessons/118645
'''