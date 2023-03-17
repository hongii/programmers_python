def solution(keymap, targets):
    res = []
    dic_keyPad = {}  # {알파벳:[알파벳 나오기 위해 누르는 횟수 , 키번호]}
    for i in range(len(keymap)):
        key = keymap[i]
        for j in range(len(key)):
            if key[j] not in dic_keyPad.keys():
                dic_keyPad[key[j]] = [j+1, i+1] # key[j]라는 알파벳을 얻기 위해서는 i+1번 키패드를 j+1번을 누른다.(i=0, j=0부터 시작하므로 1을 더한 것)
            else:
                dic_keyPad[key[j]] = min([j+1, i+1], dic_keyPad[key[j]])
    print(dic_keyPad)

    for s in targets:
        cnt = 0
        for i in range(len(s)):
            if s[i] in dic_keyPad.keys():
                cnt += dic_keyPad[s[i]][0]
            else:
                cnt = -1
                break
        res.append(cnt)

    return res