function solution(arr, k) {
    return k % 2 === 0 ? 
        arr.map(n => n+k) :
        arr.map(n => n*k)
        ;
}