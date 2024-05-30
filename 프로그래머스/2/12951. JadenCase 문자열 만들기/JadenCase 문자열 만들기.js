function solution(s) {
    var answer = [];
    
    for(let str of s.split(" ")) {
        if(str === "") {
            answer.push("");
        } else {
            answer.push(str[0].toUpperCase() + str.slice(1).toLowerCase());
        }
    }
    
    return answer.join(" ");
}
