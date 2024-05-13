function solution(arr, divisor) {
    var answer = [];
    
    arr.forEach(num => {
        if(!(num % divisor)) {
            answer.push(num);
        }
    })
    
    if(!answer.length)
        return [-1];
    
    return answer.sort((a, b) => a - b);
}