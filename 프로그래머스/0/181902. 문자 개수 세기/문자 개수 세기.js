function solution(my_string) {
    var answer = [];
    const alph = "abcdefghijklmnopqrstuvwxyz"
    const str = alph.toUpperCase() + alph;
    
    str.split("").forEach(c => {
        const regex = new RegExp(`${c}`, "g");
        const result = my_string.match(regex) ? my_string.match(regex).length : 0;
        answer.push(result)
    })
    
    return answer;
}