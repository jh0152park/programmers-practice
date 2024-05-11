function solution(num_list) {
    if(num_list.at(-1) > num_list.at(-2)) {
        return [...num_list, num_list.at(-1) - num_list.at(-2)]
    } else {
        return [...num_list, num_list.at(-1) * 2]
    }
}