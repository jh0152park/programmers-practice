function solution(my_string) {
    var answer = '';
    my_string.split("").forEach(c => {
        if(c === c.toLowerCase())
            answer += c.toUpperCase()
        else
            answer += c.toLowerCase()
    })
    return answer;
}