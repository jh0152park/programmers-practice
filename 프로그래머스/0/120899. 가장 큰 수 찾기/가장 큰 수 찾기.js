function solution(array) {
    let index = {};
    
    array.forEach((n, i) => index[n] = i);
    array.sort((a, b) => a - b)
    
    return [array.at(-1), index[array.at(-1)]];
}