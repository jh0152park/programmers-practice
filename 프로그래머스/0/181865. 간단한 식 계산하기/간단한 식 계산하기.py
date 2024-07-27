def solution(binomial):
    binomial = binomial.split(" ")
    op = binomial[1]
    num1 = int(binomial[0])
    num2 = int(binomial[2])
    
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2