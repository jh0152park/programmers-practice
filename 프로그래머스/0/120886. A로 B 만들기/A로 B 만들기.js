function solution(before, after) {
    var answer = 0;
    
    before = before.split("").sort().join("")
    after = after.split("").sort().join("")
    
    console.log(before)
    console.log(after)
    
    return before === after ? 1 : 0;
}