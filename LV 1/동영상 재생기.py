def solution(video_len, pos, op_start, op_end, commands):
    def to_seconds(time_str):
        m, s = map(int, time_str.split(":"))
        return m*60 + s
    
    video_total_sec = to_seconds(video_len)
    pos_total_sec = to_seconds(pos)
    op_start_total_sec = to_seconds(op_start)
    op_end_total_sec = to_seconds(op_end)

    if op_start_total_sec <= pos_total_sec < op_end_total_sec:
            pos_total_sec = op_end_total_sec
            
    for cmd in commands:
        if cmd == 'next':
            pos_total_sec = min(video_total_sec, pos_total_sec + 10)
        elif cmd == 'prev':
            pos_total_sec = max(0, pos_total_sec - 10)
        
        if op_start_total_sec <= pos_total_sec < op_end_total_sec:
            pos_total_sec = op_end_total_sec
            
    return str(pos_total_sec//60).zfill(2)+":"+str(pos_total_sec%60).zfill(2)
        