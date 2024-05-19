function solution(numbers, direction) {
    if(direction === "right") {
        let item = numbers.at(-1)
        numbers.pop()
        numbers.splice(0, 0, item)
        return numbers
    } else {
        let item = numbers.shift();
        numbers.push(item);
        return numbers
    }
}