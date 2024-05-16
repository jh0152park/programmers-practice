function solution(s1, s2) {
    var answer = 0;
    
    s1.forEach(c => {
        if(s2.includes(c))
            answer++;
    })
    
    return answer;
}