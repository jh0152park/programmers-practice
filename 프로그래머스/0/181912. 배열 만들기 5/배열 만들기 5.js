function solution(intStrs, k, s, l) {
    let answer = []
    intStrs.forEach(str => {
        if(+str.slice(s, s+l) > k) {
            answer.push(+str.slice(s, s+l))
        }
    })
    return answer
}