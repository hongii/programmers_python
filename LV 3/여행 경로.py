import copy
def dfs(airport, tmp, n):
    global path, res, check
    if len(tmp) == n+1:
        res.append(copy.deepcopy(tmp))

    for i, x in enumerate(path[airport]):
        if not check[airport][i] and x in path.keys():
            check[airport][i] = True
            tmp.append(x)
            dfs(x, tmp, n)
            tmp.pop()
            check[airport][i] = False

def solution(tickets):
    global path, res, check
    path, res = {}, []
    for ticket in tickets:
        if ticket[0] not in path.keys():
            path[ticket[0]] = []
        if ticket[1] not in path.keys():
            path[ticket[1]] = []
        path[ticket[0]].append(ticket[1])

    check = {key:[False]*len(path[key]) for key in path.keys()}
    dfs("ICN", ["ICN"], len(tickets))
    res.sort()
    return res[0]