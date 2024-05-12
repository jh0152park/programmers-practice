function solution(my_string, is_suffix) {
    return my_string.indexOf(is_suffix, my_string.length - is_suffix.length) < 0 ? 0 : 1
}