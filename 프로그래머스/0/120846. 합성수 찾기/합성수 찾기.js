function solution(n) {
    let numbers = [];
    
    for(let i = 4; i <= n; i++) {
        let cnt = 0;
        for(let j = 1; j <= i; j++) {
            if(i % j === 0) cnt++;
        }
        if(cnt >= 3)
            numbers.push(i)
    }
    
    return numbers.length;
}