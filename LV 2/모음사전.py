from itertools import product
def solution(word):
    l = ["A", "E", "I", "O", "U"]
    pd = []
    for i in range(1, 6):
        pd.extend(list(product(l, repeat=i)))
    pd.sort()

    w = tuple([x for x in word])
    idx = pd.index(w)

    return idx + 1