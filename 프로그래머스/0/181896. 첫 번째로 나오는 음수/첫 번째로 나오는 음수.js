function solution(num_list) {
    let index = -1;
    
    num_list.forEach((n, i) => {
        if(n < 0 && index < 0) index = i;
    })
    
    return index;
}