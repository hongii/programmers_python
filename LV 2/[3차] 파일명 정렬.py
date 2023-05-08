# re라이브러리 -> search()메서드 활용
import re
def solution(files):
    tmp = []
    idx = 0
    for file in files:
        file = file.lower()
        number = re.search('\d+', file) 
        file = [file[:number.start()], int(number.group()), file[number.end():], idx]
        tmp.append(file)
        idx += 1
    tmp.sort(key=lambda x:(x[0], x[1], x[-1]))
    res = list(map(lambda x: files[x[-1]], tmp)) # tmp배열의 각 원소에 대해, tmp 각 원소의 마지막 원소(x[-1])의 값에 해당하는 files의 값을 가져와 새로운 배열을 형성 
                                                # 정리하자면, tmp의 각 원소의 마지막 값은 files 원소의 idx값을 저장하였으므로 files[x[-1]]는 files에서 x[-1]값을 인덱스로 가지는 원소를 가져옴  

    return res

'''
# re라이브러리 메서드 알아보기
1. re.match(pattern, string, flags)
=> re.match 함수는 문자열의 처음부터 시작하여 패턴이 일치되는 것이 있는지를 확인한다.
    아래의 예시에서 첫번째는 패턴과 문자열이 동일하므로 매치되는 것을 확인할 수 있다. 이때 반환값은 match 객체를 반환한다. (값을 알아오기 위해서는 group() 메서드를 이용)
    나머지 두 개는 ‘a’로 시작하지 않아 패턴 a와 매치되지 않는다. 매치되지 않을 때 re.match 함수는 None을 반환한다.
    ex1) matchObj = re.match('a', 'a')
        print(matchObj) # 출력 결과 : <_sre.SRE_Match object; span=(0, 1), match='a'>

    ex2) print(re.match('a', 'aba')) # 출력 결과 : <_sre.SRE_Match object; span=(0, 1), match='a'>
        print(re.match('a', 'bbb')) # 출력 결과 : None
        print(re.match('a', 'baa')) # 출력 결과 : None


2. re.search(pattern, string, flags)
=> re.search 함수는 re.match와 비슷하지만, 반드시 문자열의 처음부터 일치해야 하는 것은 아니다.
    문자열의 처음뿐 아니라 중간부터라도 패턴과 일치되는 부분이 있는지를 찾는다.
    즉, 전체 문자열에서 일치하는 부분을 찾는다.
    아래의 예시 ex2에서 문자열 ‘baa’의 경우 1번째 index(두 번째 문자) ‘a’와 매치된다.
    ex1) matchObj = re.search('a', 'a')
        print(matchObj) # 출력 결과 : <_sre.SRE_Match object; span=(0, 1), match='a'>

    ex2) print(re.search('a', 'aba'))  # 출력 결과 : <_sre.SRE_Match object; span=(0, 1), match='a'>
        print(re.search('a', 'bbb')) # 출력 결과 : None
        print(re.search('a', 'baa'))  # 출력 결과 : <_sre.SRE_Match object; span=(0, 1), match='a'>


3. re.findall(pattern, string, flags)
=> re.findall 함수는 문자열 중 패턴과 일치되는 모든 부분을 찾는다.
    단, 문자열이 겹쳐지지 않게 찾는다. -> print(re.findall('aaa', 'aaaa')) 의 결과는 ['aaa', 'aaa']가 아니라, ['aaa']이다.
  ex1) matchObj = re.findall('a', 'a')
      print(matchObj) # 출력 결과 : ['a']

  ex2) print(re.findall('a', 'aba')) # 출력 결과 : ['a', 'a']
      print(re.findall('a', 'bbb')) # 출력 결과 : []
      print(re.findall('a', 'baa')) # 출력 결과 : ['a', 'a']
      print(re.findall('aaa', 'aaaa')) # 출력 결과 : ['aaa']


4. match, search object의 메서드
=> re.match(), re.search() 등의 결과로 얻은 matchObj, searchObj를 활용하는 방법
  1) group() : 일치된 문자열을 반환한다.
  2) start() : 일치된 문자열의 시작 위치를 반환한다.
  3) end() : 일치된 문자열의 끝 위치를 반환한다. (끝 위치는 포함하지 않음)
  4) span()	: 일치된 문자열의 (시작 위치, 끝 위치) 튜플을 반환한다.
  ex) matchObj = re.search('match', "'matchObj' is a good name, but 'm' is convenient.")
      print(matchObj) # 출력 결과 : <_sre.SRE_Match object; span=(1, 6), match='match'>

      print(matchObj.group()) # 출력 결과 : match
      print(matchObj.start()) # 출력 결과 : 1
      print(matchObj.end()) # 출력 결과 : 6
      print(matchObj.span()) # 출력 결과 : (1, 6) -> ‘match’가 1번째 문자부터 6번째 문자 직전까지임을 알 수 있다. (인덱스는 0부터)
'''