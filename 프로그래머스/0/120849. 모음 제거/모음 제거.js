function solution(my_string) {
    const excepts = ["a", "e", "i", "o", "u"];
    return my_string.split("").filter(c => !excepts.includes(c)).join("");
}