function solution(num_list) {
    const sort_list = num_list.sort((a,b) => a-b);
    return sort_list.slice(0,5);
}