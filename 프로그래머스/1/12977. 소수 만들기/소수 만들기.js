function combinations(items, set) {
    if(set === 1) {
        return items.map((item) => [item]);
    }
    
    let results = [];
    items.forEach((item, index) => {
        let left = items.slice(index + 1);
        let combination = combinations(left, set - 1);
        combination.forEach((combi) => results.push([item, ...combi]));
    })
    
    return results;
}


function is_prime(num) {
    for(let i = 2; i <= Math.sqrt(num); i++) {
        if(!(num % i)) {
            return false;
        }
    }
    return true;
}


function get_sum(nums) {
    return nums[0] + nums[1] + nums[2];
}


function solution(nums) {
    var answer = 0;
    let prime_combinations = combinations(nums, 3);
    
    for(let i = 0; i < prime_combinations.length; i++) {
        if(is_prime(get_sum(prime_combinations[i]))) {
            answer++;
        }
    }
    
    return answer;
}