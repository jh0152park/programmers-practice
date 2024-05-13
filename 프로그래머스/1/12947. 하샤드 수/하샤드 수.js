function solution(x) {
    let sum = 0;
    
    String(x).split("").forEach(n => sum += +n);
    return x % sum ? false : true;
}