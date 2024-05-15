function solution(myString) {
    return myString.split("").map((s) => "l" > s ? "l" : s).join("");
}