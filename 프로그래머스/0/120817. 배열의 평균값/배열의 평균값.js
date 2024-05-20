function solution(numbers) {
    var answer = 0;
    numbers.forEach(n => answer += n)
    return answer / numbers.length;
}