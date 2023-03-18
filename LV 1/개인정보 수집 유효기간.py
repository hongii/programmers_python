def expirationDate(info, term):
    y, m, d = int(info[:4]), int(info[5:7]), int(info[8:10])
    d = d-1 or 28
    if d == 28:
        m -= 1
    y = y + (m+term)//12 
    m = (m+term) % 12 or 12
    if m == 12:
        y -= 1
        
    return y, m, d
    
def solution(today, terms, privacies):
    dic_terms = {}
    res = []
    for x in terms:
        if x[0] not in dic_terms.keys():
            dic_terms[x[0]] = int(x[2:])
    # print(dic_terms)
    
    year, month, day = int(today[:4]), int(today[5:7]), int(today[8:])
    for idx, info in enumerate(privacies):
        term = dic_terms[info[-1]]
        y, m, d = expirationDate(info, term)
        # print(y, m, d)
        if y < year:
            res.append(idx+1)
        elif y == year and m < month:
            res.append(idx+1)
        elif y == year and m == month and d < day:
            res.append(idx+1)
            
    return res