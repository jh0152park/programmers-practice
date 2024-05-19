function solution(numbers, k) {
    var answer = 0;
    
    if(k === 1)
        return numbers[0];
    
    
    
    return numbers[parseInt(((k-1)*2)%numbers.length)];
}