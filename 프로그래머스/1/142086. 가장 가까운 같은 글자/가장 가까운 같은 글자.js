function solution(s) {
    let chars = {};
    let answer = [];
    
    for(let i = 1; i <= s.length; i++) {
        let char = s[i - 1];

        if(!(!!chars[char])) {
            answer.push(-1);
            chars[char] = i;
        } else {
            answer.push(i - chars[char]);
            chars[char] = i;
        }
    }
    
    return answer;
}