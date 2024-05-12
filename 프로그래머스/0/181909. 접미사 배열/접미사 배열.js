function solution(my_string) {
    return my_string.split("").map((s, i) => my_string.slice(i)).sort();
}