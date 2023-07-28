### 2회차 풀이 ###
from itertools import permutations
import re
def calculate(a, b, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    
def solution(expression):
    expList = re.split("([\*\-\+])", expression)
    ops = set([x for x in expList if not x.isdecimal()])
    pm = list(permutations(ops))
    
    maxRes = 0
    for p in pm:
        res = 0
        tmp = expList.copy()
        for op in p:
            while len(tmp) > 1 and op in tmp:
                idx = tmp.index(op)
                num = calculate(int(tmp[idx-1]), int(tmp[idx+1]), op)
                tmp = tmp[:idx-1] + [num] + tmp[idx+2:]
        if maxRes < abs(tmp[0]):
            maxRes = abs(tmp[0])
    return maxRes


### 1회차 풀이 ###
from itertools import permutations
import re

# op 연산자에 해당하는 연산자로 계산하는 함수
def calc(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    
def solution(expression):
    # expression에 포함되어 있는 연산자를 ops배열에 추가하기(우선순위 순열을 구하기 위함)
    ops = []
    if "+" in expression:
        ops.append("+")
    if "-" in expression:
        ops.append("-")
    if "*" in expression:
        ops.append("*")
    pm = list(permutations(ops, len(ops))) # 연산자 우선순위 순열 구하기
    
    ex = re.split('([\+\-\*])', expression) # re라이브러리를 이용하여 문자열을 여러개의 구분자로 분할하기

    maxRes = 0
    for t in pm: # 연산자 우선순위 순열 하나씩 가져오기
        tmp = ex
        for op in t: # 우선순위가 높은 연산자부터 하나씩 계산
            s = []
            check = 0 # 계산 했는지 안했는지 확인하는 flag (ex[i+1]숫자는 이미 직전에 계산되어서 다음 반복문때 s에 해당 숫자(ex[i+1])를 넣지 않아야 하므로)
            for i in range(len(tmp)):
                if check: # 앞에서 이미 계산된 숫자이므로 패스
                    check = 0
                    continue
                if tmp[i] == op:
                    num = calc(int(s.pop()), int(tmp[i+1]), op)
                    s.append(num)
                    check = 1
                else:
                    s.append(tmp[i])
            tmp = s # 우선순위가 가장 높은 연산자부터 계산한 결과 스택(ex. 연산자 우선순위가 *,+,-순이라면 위의 반복문이 종료되면 *연산자는 전부 계산되어 +,-연산자만 s에 남아있다.)
        
        if abs(s[0]) > maxRes:
            maxRes = abs(s[0])
    
    return maxRes

'''
# re 라이브러리를 활용하여 여러개의 구분자로 문자열 분할하기 -> 정규식 표현을 구분자로
ex1) 정규식에 사용되는 표현들(+, *, -, ?, ^ 등...)을 구분자 문자 그 자체로 사용하기 위해서는, "\" 백슬래시 기호를 해당 문자 앞에 적어주면 된다. 
      즉, \+ 를 적어주면 \가 한 번 이상 쓰였는지를 판단하는 것이 아니라 문자 그대로인 "+"와 일치하는지 검사하게 된다.
      (정규식에서의 + 의미: 문자 그룹이나 바로 앞 문자가 한번 이상 반복될 수 있다는 것을 의미) 
expression = "100-200*300-500+20"
print (re.split('[\+\-\*]', expression)) # 출력 : ['100', '200', '300', '500', '20']

ex2) 구분자를 포함하여 리스트를 만들고 싶다면, 구분자 그룹인 [] 대괄호를 소괄호로 감싸주면 된다.
expression = "100-200*300-500+20"
print (re.split('([\+\-\*])', expression)) # 출력 : ['100', '-', '200', '*', '300', '-', '500', '+', '20']
'''