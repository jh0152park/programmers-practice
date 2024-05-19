function solution(n, k) {
    const service = parseInt(n / 10);
    const drink = k - service;
    return (n * 12000) + (drink * 2000);
}