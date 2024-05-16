function solution(n) {
    let answer = []
    
    for(let i = 0; i < n; i++)
        answer.push([...Array(n).fill(0)])

    let i = 0, j = -1, cnt = 0, sw = 1;
    
    while(true) {
        for(let k = 0; k < n; k++) {
            cnt++;
            j += sw;
            answer[i][j] = cnt;
        }
        n--;
        if(n <= 0) break;
        for(let z = 0; z < n; z++) {
            cnt++;
            i += sw;
            answer[i][j] = cnt;
        }
        sw *= -1;
    }
    
    
    return answer;
}