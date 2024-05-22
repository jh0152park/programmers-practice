/*
a = 97
A = 65
z = 122
Z = 90
*/
function solution(s, n) {
    var answer = '';
    
    for(let char of s.split("")) {
        if(char === " ") {
            answer += char;
        } else {
            let code = char.charCodeAt();
            if(code >= 97 && code <= 122) {
                code += n;
                if(code > 122) code -= 26;
            } else {
                code += n;
                if(code > 90) code -= 26;
            }
            answer += String.fromCharCode(code);
        }
    }
    
    return answer;
}