function solution(arr) {
    var answer = [];
    arr.forEach((n) => answer = [...answer, ...Array(n).fill(n)])
    return answer;
}