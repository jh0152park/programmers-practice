function solution(array, n) {
    let diff = array.sort((a, b) => a - b).map(num => Math.abs(n-num));    
    let min = Math.min(...diff)

    return array[diff.indexOf(min)];
}

// array = [20, 10], n = 15
// result -> 10