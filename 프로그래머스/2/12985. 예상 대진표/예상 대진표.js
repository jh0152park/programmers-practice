function solution(n,a,b)
{
    let answer = 0;
    
    // 처음 A번인 선수가 경쟁자인 B선수를 몇번째 라운드에서 만날까요?
    // 4 / 7
    // 2 / 4
    // 1 / 2
    while(a != b) {
        answer++;
        console.log(a, b);
        a = Math.round(a / 2);
        b = Math.round(b / 2);
    }
    
    return answer;
}