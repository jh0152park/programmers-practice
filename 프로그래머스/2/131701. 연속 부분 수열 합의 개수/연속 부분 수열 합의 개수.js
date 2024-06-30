function solution(elements) {
    let numbers = {};
    let length = elements.length;
    
    
    for(let i = 1; i < length; i++) {
        for(let j = 0; j < length; j++) {
            let sum = 0;
            for(let k = j; k < i + j; k++) {
                sum += elements[Math.floor(k % length)];
            }
            numbers[sum] = true;
        }
    }
    
    // console.log(Object.keys(numbers).sort((a, b) => a - b));
    
    return Object.keys(numbers).length + 1;
}