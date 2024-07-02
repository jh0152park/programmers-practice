var BRACKET = {
    "[": true,
    "(": true,
    "{": true,
    "]": false,
    ")": false,
    "}": false,
};

var PARI = {
    "]": "[",
    ")": "(",
    "}": "{",
}

function is_correct(bracket) {
    let stack = [];
    let current = "";
    let length = bracket.length;
    
    if(length % 2) {
        return false;
    }
    
    for(let i = 0; i < bracket.length; i++) {
        current = bracket[i];
        
        if(BRACKET[current]) {
            stack.push(current);
            continue;
        } 
        
        if(stack.length === 0) {
            // stact underflow
            return false;
        }
        
        if(stack.at(-1) !== PARI[current]) {
            return false;
        }
        stack.pop();
    }
    
    return true;
}

function solution(s) {
    var answer = 0;
    let length = s.length;
    
    for(let shift = 0; shift < length; shift++) {
        if(is_correct(s)) {
            answer++;
        }
        s = s.slice(1) + s[0];
    }
    
    return answer;
}