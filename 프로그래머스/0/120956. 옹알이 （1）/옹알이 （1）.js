function solution(babbling) {
    let answer = 0;
    const words = ["aya", "ye", "woo", "ma"];
    
    for(let i = 0; i < babbling.length; i++) {
        for(let word of words) {
            babbling[i] = babbling[i].replaceAll(word, "*")
        }
        babbling[i] = babbling[i].replaceAll("*", "")
        if(babbling[i] === "") answer++;
    }
    return answer;
}