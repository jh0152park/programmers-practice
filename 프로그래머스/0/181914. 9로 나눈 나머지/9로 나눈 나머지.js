function solution(number) {
    let sum = 0;
    
    number.split("").forEach(n => sum += +n)
    return sum % 9;
}