function solution(my_string, indices) {
    return my_string.split("").filter((c,i) => !indices.includes(i) ? c : null).join("");
}