function solution(new_id) {
    var answer = '';
    let special_character = {
        "-": true, "_": true, ".": true
    }
    
    // step 1 + 2
    for(let char of new_id) {
        // 소문자
        if(char.charCodeAt() >= 97 && char.charCodeAt() <= 122) {
            answer += char;
        }
        // 대문자
        else if(char.charCodeAt() >= 65 && char.charCodeAt() <= 90) {
            answer += char.toLowerCase();
        }
        // 유효한 특수문자
        else if(!!special_character[char]) {
            answer += char;
        }
        // 숫자일 경우
        else if(!isNaN(+char)) {
            answer += char;
        }
    }
    
    // step 3
    let temp = [];
    for(let char of answer) {
        temp.push(char);
        if(temp.length >= 2) {
            if(temp.at(-2) === "." && temp.at(-1) === ".") {
                temp.pop();
            }
        }
    }
    
    // step 4
    if(temp[0] === ".") {
        temp.shift();
    }
    if(temp.at(-1) === ".") {
        temp.pop();
    }
    
    
    // step 5
    if(temp.length === 0) {
        return "aaa";
    }
    
    // step 6
    if(temp.length >= 16) {
        temp = temp.slice(0, 15);
        if(temp[0] === ".") {
            temp.shift();
        }
        if(temp.at(-1) === ".") {
            temp.pop();
        }
    }
    
    // step 7
    if(temp.length <= 2) {
        while(temp.length !== 3) {
            temp.push(temp.at(-1));
        }
    }
        
    return temp.join("");
}