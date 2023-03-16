# from string import ascii_lowercase
def solution(new_id):
    alphabet_list = [chr(i) for i in range(ord("a"), ord("z")+1)] # 또는 string모듈에서 ascii_lowercase를 import한 후에, alphabet_list = list(ascii_lowercase) 사용
    number_list = [str(i) for i in range(10)]
    etc = ["-", "_", "."]

    new_id = new_id.lower() # 1단계

    for i in range(len(new_id)): # 2단계
        if new_id[i] not in (alphabet_list + number_list + etc):
            new_id = new_id.replace(new_id[i], " ")
    new_id = new_id.replace(" ","")

    while ".." in new_id: # 3단계
        new_id = new_id.replace("..", ".")

    if len(new_id) > 0 and new_id[0] == ".": # 4단계
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == ".":
        new_id = new_id[:-1]

    if new_id == "": # 5단계
        new_id = "a"

    if len(new_id) >= 16: # 6단계
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    if len(new_id) <= 2: # 7단계
        new_id += new_id[-1] * (3 - len(new_id))

    return new_id

''' 정규식을 이용한 풀이
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
'''