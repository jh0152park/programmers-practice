function solution(str_list, ex) {
    const filter_string = str_list.filter((str) => !str.includes(ex));
    return filter_string.join("");
}