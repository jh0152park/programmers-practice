function solution(array) {
    var answer = 0;
    
    array.join("").split("").forEach(n => {
        if(n==="7") answer++;
    })
    
    return answer;
}