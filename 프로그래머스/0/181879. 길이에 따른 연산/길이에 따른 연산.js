function allSum(list) {
    let sum = 0;
    list.forEach(n => sum += n);
    return sum;
}

function allMul(list) {
    let mul = 1;
    list.forEach(n => mul *= n);
    return mul;
}

function solution(num_list) {
    return num_list.length >= 11 ? allSum(num_list) : allMul(num_list)
}