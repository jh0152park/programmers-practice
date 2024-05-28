function permutations(items, set) {
    if(set === 1) {
        return items.map((item) => [item]);
    }
    
    let results = [];
    items.forEach((item, index) => {
        let left = [...items.slice(0, index), ...items.slice(index + 1)];
        let permutation = permutations(left, set - 1);
        permutation.forEach((combi) => results.push([item, ...combi]));
    })
    
    return results;
}


function convert_to_number(string_numbers) {
    return Number(string_numbers.join(""));
}


function is_prime_number(number) {
    if(number < 2) {
        return false;
    }
    
    for(let i = 2; i <= Math.sqrt(number); i++) {
        if(!(number % i)) {
            return false;
        }
    }
    
    return true;
}


function solution(numbers) {
    let answer = 0;
    let length = numbers.length;
    let entire_combinations = {};
    
    numbers = numbers.split("");
    
    for(let i = 1; i <= length; i++) {
        for(let permunation of permutations(numbers, i)) {
            let number = convert_to_number(permunation);
            
            if(!(!!entire_combinations[number])) {
                entire_combinations[number] = true;
                if(is_prime_number(number)) {
                    answer++;
                }
            }
        }
    }
    
    return answer;
}