from collections import Counter
def solution(genres, plays):
    totalPlay = {key:0 for key in genres}
    genre_idx = {key:[] for key in genres}
    for i in range(len(plays)):
        totalPlay[genres[i]] += plays[i]
        genre_idx[genres[i]].append([plays[i],i])

    sortedPlays = Counter(totalPlay).most_common()

    for value in genre_idx.values():
        value.sort(key=lambda x: x[0], reverse=True)

    res = []
    for (genre, totalCnt) in sortedPlays:
        res.append(genre_idx[genre][0][1])
        if len(genre_idx[genre]) > 1:
            res.append(genre_idx[genre][1][1])
    return res        