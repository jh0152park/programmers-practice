function solution(n, k) {
    var answer = [];
    for(let i = 1; i <= n; i++)
        if(!(i % k)) answer.push(i)
    return answer;
}