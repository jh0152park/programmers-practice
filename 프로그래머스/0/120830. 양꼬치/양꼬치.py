def solution(n, k):
    drink = n // 10;
    return (n * 12000) + ((k-drink) * 2000)