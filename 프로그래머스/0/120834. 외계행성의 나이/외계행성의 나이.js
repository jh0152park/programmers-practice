function solution(age) {
    let answer = ""
    let alph = "abcdefghijklmnopqrstuvwxyz";
    alph = alph.split("");
    
    [...age.toString()].forEach(n => {
        answer += alph[+n]
    })
    
    return answer;
}