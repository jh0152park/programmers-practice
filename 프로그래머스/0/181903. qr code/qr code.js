function solution(q, r, code) {
    return code.split("").filter((c, i) => (i % q === r)).join("");
}