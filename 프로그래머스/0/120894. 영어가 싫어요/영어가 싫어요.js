function solution(numbers) {
    var answer = 0;
    const eng_nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for(let i = 0; i < eng_nums.length; i++) {
        numbers = numbers.replaceAll(eng_nums[i], i+"")
    }
    
    console.log(numbers)
    
    
    return +numbers;
}