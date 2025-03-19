def solution(diffs, times, limit):
    
    def can_complete(level):
        time_sum = 0
        for i in range(len(diffs)):
            if diffs[i] <= level:
                time_sum += times[i]
            else:
                time_sum += (times[i] + times[i-1]) * (diffs[i] - level) + times[i]

            if time_sum > limit:
                return False
        
        return True

    left, right = 1, max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_complete(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer