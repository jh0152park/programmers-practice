function oper(num) {
    switch(num) {
        case 1:
            return "w";
        case -1:
            return "s";
        case 10:
            return "d";
        case -10:
            return "a"
    }
}

function solution(numLog) {
    var answer = "";
    
    for(let i = 1; i < numLog.length; i++) {
        answer += oper(numLog[i] - numLog[i-1])
    }
    
    return answer;
}