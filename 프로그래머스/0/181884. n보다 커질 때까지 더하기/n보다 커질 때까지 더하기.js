function solution(numbers, n) {
    let sum = 0;
    for(num of numbers) {
        if(sum > n) return sum;
        sum += num;
    }
    return sum;
}