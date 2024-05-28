function solution(s) {
    let x = "";
    let same = 0;
    let diff = 0;
    var answer = 0;
    
    for(let char of s) {
        if(x === "") {
            x = char;
            same++;
            continue;
        }
        
        if(x === char) {
            same++;
        } else {
            diff++;
        }
        
        if(same === diff) {
            answer++;
            same = 0;
            diff = 0;
            x = "";
        }
    }
        
    return same + diff === 0 ? answer : answer + 1;
}