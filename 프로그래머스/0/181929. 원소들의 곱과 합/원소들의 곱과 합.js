function solution(num_list) {
    let sum = 0;
    let mul = 1;
    
    num_list.forEach((n) => {
        sum += n;
        mul *= n;
    })
    
    return mul < sum * sum ? 1 : 0
}