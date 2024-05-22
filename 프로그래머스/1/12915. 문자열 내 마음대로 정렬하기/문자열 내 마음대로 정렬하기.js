function solution(strings, n) {
    let code = [];
    var answer = [];
    
    for(let word of strings) {
        code.push(word[n].charCodeAt());
    }    
    
    code = Array.from(new Set(code));
    code = code.sort((a, b) => a - b);

    while(code.length > 0) {
        let sameWords = [];
        let minCode = code.shift();
        for(let word of strings) {
            if(word[n].charCodeAt() === minCode) {
                sameWords.push(word);
            }
        }
        
        sameWords.sort();
        answer.push(...sameWords);
    }
    
    return answer;
}