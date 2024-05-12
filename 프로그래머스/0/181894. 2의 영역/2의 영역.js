function solution(arr) {
    if(!arr.includes(2))    return [-1];
    
    const start = arr.indexOf(2);
    const last = arr.lastIndexOf(2);
    
    return arr.slice(start,last+1)
}