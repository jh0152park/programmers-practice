function solution(n) {
    return +(String(n).split("").map(n => +n)).sort((a, b) => b - a).join("");
}