def solution(a, b, n):
    cola = 0
    while n >= a:
        remainder = n % a 
        cola += (n//a) * b
        n = (n//a) * b + remainder
    return cola