function solution(s) {
    let max = -9999;
    let min = 9999;
    
    for(let num of s.split(" ")) {
        if(+num > max)  max = +num;
        if(+num < min)  min = +num;
    }
    
    return `${min} ${max}`;
}