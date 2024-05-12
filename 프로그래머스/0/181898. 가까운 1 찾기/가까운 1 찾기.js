function solution(arr, idx) {
    return arr.slice(idx).indexOf(1) < 0 ? -1 : arr.slice(idx).indexOf(1) + idx;
}