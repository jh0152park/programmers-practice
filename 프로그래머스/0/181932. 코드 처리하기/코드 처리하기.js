function solution(code) {
    var answer = '';
    let mode = false;
    
    code.split("").forEach((c, i) => {
        if(c === "1") {
            mode = !mode;
        } else {
            if(mode) {
                if(i % 2) {
                    answer += c;
                }
            } else {
                if(!(i % 2)) {
                    answer += c;
                }
            }
        }
    })
    
    return answer === "" ? "EMPTY" : answer;
}