function solution(my_string, m, c) {
    var answer = '';
    
    while(c <= my_string.length) {
        answer += my_string[c-1];
        c += m;
    }
    
    return answer;
}

