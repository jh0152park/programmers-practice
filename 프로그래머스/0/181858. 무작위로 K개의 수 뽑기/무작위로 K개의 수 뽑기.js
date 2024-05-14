function solution(arr, k) {
    let new_arr = Array.from(new Set(arr));
    
    console.log(new_arr);
    
    if(new_arr.length >= k)
        return new_arr.slice(0, k);
    
    const diff = k - new_arr.length;
    console.log(diff)
    for(let i = 0; i < diff; i++)
        new_arr.push(-1);
    
    return new_arr;
}