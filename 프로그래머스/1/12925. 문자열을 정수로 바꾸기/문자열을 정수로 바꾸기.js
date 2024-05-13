function solution(s) {
    return s.startsWith("-") ? +s.slice(1) * -1 : +s;
}