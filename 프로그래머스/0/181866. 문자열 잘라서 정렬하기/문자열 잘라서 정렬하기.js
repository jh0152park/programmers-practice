function solution(myString) {
    return myString.split("x").sort().filter(c => c !== "");
}