function how_many_sum(target) {
    let hit = 0;
    let nums = new Array(target).fill(0);

    for(let i = 1; i <= target; i++) {
        nums[i - 1] = i;
    }

    for(let i = 0; i < target; i++) {
        let sum = 0;
        for(let j = i; j < target; j++) {
            sum += nums[j];

            if(sum > target) {
                break;
            }

            if(sum === target) {
                hit++;
            }
        }
    }

    return hit;
}


function solution(n) {
    return how_many_sum(n);
}