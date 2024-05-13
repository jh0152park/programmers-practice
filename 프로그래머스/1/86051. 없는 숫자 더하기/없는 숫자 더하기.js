function solution(numbers) {
    var answer = 0;
    const nums = new Array(10).fill(0);

    for(let i = 0; i < numbers.length; i++) {
        nums[numbers[i]]++;
    }
    
    for(let i = 0; i < 10; i++) {
        if(!nums[i]) {
            answer += i;
        }
    }
    
    return answer;
}