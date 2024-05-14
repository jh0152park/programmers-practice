function solution(arr1, arr2) {
    if(arr1.length !== arr2.length) {
        return arr1.length > arr2.length ? 1 : -1;
    }
    
    let arr1_sum = 0;
    let arr2_sum = 0;
    
    arr1.forEach(n => arr1_sum += n);
    arr2.forEach(n => arr2_sum += n);
    
    return arr1_sum === arr2_sum ? 0 : arr1_sum > arr2_sum ? 1 : -1;
}