
def solution(a, b):
    weeks = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    monthDays = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totalDays = sum(monthDays[:a]) + b
    return weeks[totalDays % 7]
