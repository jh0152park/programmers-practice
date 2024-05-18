function solution(order) {
    var answer = 0;
    let numbers = ["3", "6", "9"]
    
    
    
    order.toString().split("").forEach(n => {
        if(numbers.includes(n))
            answer++;
    })
    
    return answer;
}