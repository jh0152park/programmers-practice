function solution(my_string, overwrite_string, s) {
    const str = my_string.split("")
    return [...my_string.slice(0, s), ...overwrite_string.split(""), ...str.slice(s + overwrite_string.length)].join("")
}