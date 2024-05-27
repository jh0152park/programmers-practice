function solution(babbling) {
    var answer = 0;
    let pronounces = ["aya", "ye", "woo", "ma"];
    
    
    for(let word of babbling) {
        let prev = "";
        let chars = "";
        
        for(let char of word) {
            chars += char;
            
            if(prev === chars) {
                break;
            }
            
            if(pronounces.includes(chars)) {
                prev = chars;
                chars = "";
            }
        }
        
        if(chars === "") {
            answer++;
        }
    }
    
    return answer;
}