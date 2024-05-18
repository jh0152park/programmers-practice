function solution(my_string, num1, num2) {
    let char1 = my_string[num1];
    let char2 = my_string[num2];
    let str = my_string.split("");
    str[num1] = char2;
    str[num2] = char1;
    return str.join("");
}