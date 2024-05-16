function solution(my_str, n) {
    var answer = [];
    let str = "";
    
    for(let i = 0; i < my_str.length; i++) {
        str += my_str[i];
        if(str.length === n) {
            answer.push(str);
            str = ""
        }
    }
    
    if(str !== "")
        answer.push(str);
    
    return answer;
}