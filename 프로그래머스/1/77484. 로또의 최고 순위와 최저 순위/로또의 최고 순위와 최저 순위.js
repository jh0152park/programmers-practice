function compute_match(lottos, win_nums) {
    let match = 0;
    let available = 0;
    
    for(let number of lottos) {
        if(number !== 0) {
            if(win_nums.includes(number)) {
                match++;
            }
        } else {
            available++;
        }
    }
    
    return {match, available};
}


function solution(lottos, win_nums) {
    let {match, available} = compute_match(lottos, win_nums);
    let rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
        
    return [rank[match + available], rank[match]];
}