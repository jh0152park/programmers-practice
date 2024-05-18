function solution(cipher, code) {
    var answer = '';
    cipher.split("").forEach((c, i) => {
        if((i + 1) % code === 0)
            answer += c;
    })
    return answer;
}