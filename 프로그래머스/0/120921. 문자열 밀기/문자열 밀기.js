function shift(str) {
    let last = ""
    
    str = str.split("")
    last = str.pop()
    str.splice(0, 0, last);
    return str.join("")
}

function solution(A, B) {
    var answer = 0;

    
    if(A === B) return 0;
    
    for(let i = 0; i < A.length; i++) {
        A = shift(A);
        answer++;
        if(A === B) return answer;
    }
    
    return -1;
}