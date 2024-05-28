function solution(dartResult) {
    let index = 0;
    let score = "";
    let scores = [-1, -1, -1];
    let options = ["*", "#"];
    let bonus = ["S", "D", "T"];
    let pows = {
        "S": 1,
        "D": 2,
        "T": 3,
    };
    
    
    for(let char of dartResult) {
        if(!options.includes(char) && !bonus.includes(char)) {
            score += char;
        } else {
            if(score !== "") {
                scores[index++] = +score;
                score = "";
            }
            
            if(bonus.includes(char)) {
                scores[index - 1] = scores[index - 1] ** pows[char];
            } else if(options.includes(char)) {
                if(char === "#") {
                    scores[index - 1] *= -1;
                } else {
                    if(index === 1) {
                        scores[0] *= 2;
                    } else {
                        scores[index - 1] *= 2;
                        scores[index - 2] *= 2;
                    }
                }
            }
        }
    }
        
    return scores[0] + scores[1] + scores[2];
}