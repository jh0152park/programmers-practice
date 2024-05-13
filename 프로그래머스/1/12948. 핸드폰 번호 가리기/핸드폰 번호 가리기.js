function solution(phone_number) {
    let star = "*";
    let length = phone_number.length;
    return `${star.repeat(length - 4)}${phone_number.slice(length - 4)}`
}