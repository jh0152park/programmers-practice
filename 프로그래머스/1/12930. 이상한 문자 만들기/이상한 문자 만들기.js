function solution(s) {
    var answer = '';
    
    for(let str of s.split(" ")) {
        let word = "";
        for(let i = 0; i < str.length; i++) {
            if(i % 2) {
                word += str[i].toLowerCase();
            } else {
                word += str[i].toUpperCase();
            }
        }
        answer += word + " ";
    }
    
    return answer.slice(0, answer.length - 1);
}