import math
def solution(n, w, num):
    rows = math.ceil(n/w)
    val = 1
    arr = []
    for r in range(rows):
        line = list(range(val, min(val+w, n+1)))
        line += [0] * (w - len(line))
        if r % 2 == 1:
            line.reverse()
        arr.append(line)
        val += w

    for r, row in enumerate(arr):
        if num in row:
            c = row.index(num)
            break

    count = 0
    for line in reversed(arr):
        if line[c] == num:
            break
        if line[c] != 0:
            count += 1

    return count + 1