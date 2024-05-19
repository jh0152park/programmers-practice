function solution(my_string, letter) {
    return my_string.split("").filter(c => c !== letter).join("");
}