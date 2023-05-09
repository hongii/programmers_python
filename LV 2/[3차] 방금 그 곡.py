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