function solution(a, d, included) {
    var answer = 0;
    included.forEach((b, i) => b ? answer += (i*d)+a : null)
    return answer;
}