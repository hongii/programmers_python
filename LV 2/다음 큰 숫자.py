def solution(n):
    nToBin = bin(n)[2:].count("1")
    while True:
        n += 1
        if nToBin == bin(n)[2:].count("1"):
            return n
            