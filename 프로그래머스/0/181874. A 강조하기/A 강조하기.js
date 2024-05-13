function solution(myString) {
    myString = myString.split("").map((s) => s === s.toUpperCase() ? s.toLowerCase() : s)
    return myString.join("").replaceAll("a", "A");
}