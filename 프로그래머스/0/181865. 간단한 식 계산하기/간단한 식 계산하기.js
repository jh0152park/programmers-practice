function calc(oper, num1, num2) {
    switch(oper) {
        case "+":
            return num1 + num2;
        case "-":
            return num1 - num2;
        case "*":
            return num1 * num2;
    }
}

function solution(binomial) {
    const str = binomial.split(" ");
    return calc(str[1], +str[0], +str[2]);
}