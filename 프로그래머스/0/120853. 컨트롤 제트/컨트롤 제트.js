function solution(s) {
    var answer = 0;
    let nums = []
    
    s.split(" ").forEach(n => {
        if(n === "Z") {
            nums.pop()
        } else {
            nums.push(n)
        }
    })
    
    nums.forEach(n => answer += +n)
    
    return answer;
}