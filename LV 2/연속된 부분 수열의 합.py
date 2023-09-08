# 투포인터
def solution(sequence, k):
    seq_len = len(sequence)
    idx_s, idx_e = 0, len(sequence)-1
    rt = 0
    seq_sum = 0
    for lt in range(len(sequence)):
        while seq_sum < k and rt < len(sequence):
            seq_sum += sequence[rt]
            rt += 1

        if seq_sum == k:
            if seq_len > rt-lt:
                seq_len = rt-lt
                idx_s, idx_e = lt, rt-1
        seq_sum -= sequence[lt]

    return [idx_s, idx_e]