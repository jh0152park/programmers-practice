function solution(n)
{
    var answer = 0;

    String(n).split("").forEach(c => answer += +c);
    
    return answer;
}