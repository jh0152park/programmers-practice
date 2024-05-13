function solution(s) {
    const length = s.length;
    const center = Math.floor(length / 2);
    return length % 2 ? s[center] : s.slice(center - 1, center + 1);
}