function solution(numbers) {
    numbers.sort((a,b) => a-b);
    return numbers[0] * numbers[1] > numbers.at(-1) * numbers.at(-2) ? numbers[0] * numbers[1] : numbers.at(-1) * numbers.at(-2);
}