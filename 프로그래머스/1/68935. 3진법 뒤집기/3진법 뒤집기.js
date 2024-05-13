function get_three(n) {
    const nums = [];
    
    while(n) {
        nums.push(n % 3);
        n = Math.floor(n / 3);
    }
    
    return nums;
}

function convert_3_to_10(nums) {
    let num = 0;
    
    for(let i = 0; i < nums.length; i++) {
        num += (3 ** (nums.length - 1 - i)) * nums[i];
    }
    
    return num;
}

function solution(n) {
    return convert_3_to_10(get_three(n));
}
