function solution(array) {
    let count_array = [...Array(Math.max(...array)+1).fill(0)];
    
    array.forEach(n => count_array[n]++)
    
    const max = Math.max(...count_array);
    const max_index = count_array.indexOf(max);
    count_array.splice(max_index, 1);
    const max2 = Math.max(...count_array);
    
    return max === max2 ? -1 : max_index;
}