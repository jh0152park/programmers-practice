function solution(strArr) {
    return strArr.map((str, index) => !(index % 2) ? str.toLowerCase() : str.toUpperCase());
}