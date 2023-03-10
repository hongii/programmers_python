def solution(sizes):
    maxWidth, maxHeight = 0, 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] =  sizes[i][1], sizes[i][0]
        if maxWidth < sizes[i][0]:
            maxWidth = sizes[i][0]
        if maxHeight < sizes[i][1]:
            maxHeight = sizes[i][1]
    return maxWidth * maxHeight

'''최적의 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
'''