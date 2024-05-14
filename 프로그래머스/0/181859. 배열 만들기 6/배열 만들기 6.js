function solution(arr) {
    var answer = [arr[0]];
    
    for(let i = 1; i < arr.length; i++) {
        if(answer.at(-1) === arr[i]) {
            answer.pop();
        } else if(answer.at(-1) !== arr[i]) {
            answer.push(arr[i])
        }
    }
    
    return answer.length ? answer : [-1];
}