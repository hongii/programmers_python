# 2회차 코드
import re
def solution(m, musicinfos):
    res = []
    m = m.replace("C#","c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#","a")
    for i, info in enumerate(musicinfos):
        infoList = info.split(",")
        start_h, start_m = int(infoList[0][:2]), int(infoList[0][3:])
        end_h, end_m = int(infoList[1][:2]), int(infoList[1][3:])
        playTime = (end_h*60 + end_m) - (start_h*60 + start_m)
        title, codes = infoList[2], infoList[3]
        codes = codes.replace("C#","c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#","a")
        if playTime > len(codes):
            repeat = playTime//len(codes) + 1
            codes = codes * repeat
            
        if re.search(m, codes[:playTime]):
            res.append((playTime, i, title))
    
    return sorted(res, key=lambda x:(-x[0], x[1]))[0][2] if len(res) > 0 else "(None)"


# 1회차 코드
import math
import re
def solution(m, musicinfos):
    m = m.replace("A#", "a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")
    dic = {m:[]}

    for idx, music in enumerate(musicinfos):
        musicInfo = music.split(",")
        h_s, m_s, h_e, m_e = int(musicInfo[0][:2]), int(musicInfo[0][3:5]), int(musicInfo[1][:2]), int(musicInfo[1][3:5])
        playTime = (h_e*60 + m_e) - (h_s*60 + m_s)
        title = musicInfo[2]
        code = musicInfo[3].replace("A#", "a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")
        playCode = code * math.ceil(playTime / len(code)) if len(code) < playTime else code[:playTime]
        # print(playTime,title, playCode)

        res = re.search(m, playCode) 
        if res != None: # 실행된 코드에서(playCode) 찾고자 하는 코드(m)와 일치하는 코드가 존재한다면
            dic[m].append([title, playTime, idx]) 

    dic[m].sort(key=lambda x:(-x[1], x[2])) # 실행시간(playTime)이 긴 순서대로, 실행시간이 같다면 먼저 입력된 순서대로(idx)
    return dic[m][0][0] if len(dic[m]) > 0 else "(None)"