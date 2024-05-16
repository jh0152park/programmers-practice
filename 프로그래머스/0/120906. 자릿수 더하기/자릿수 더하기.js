function solution(n) {
    var answer = 0;
    // [...n.toString()].forEach(num => answer += num)
    [...n.toString()].forEach(n => answer += +n)
    return answer;
}