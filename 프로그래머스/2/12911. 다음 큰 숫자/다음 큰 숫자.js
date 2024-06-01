function count_one(bin) {
    let one = 0;
    
    for(let num of bin) {
        if(num === "1") {
            one++;
        }
    }
    
    return one;
}


function solution(n) {
    var answer = 0;
    let one_of_n = count_one(n.toString(2));
    
    for(let i = n + 1; i <= 1000000; i++) {
        if(one_of_n === count_one(i.toString(2))) {
            return i;
        }
    }
    
}