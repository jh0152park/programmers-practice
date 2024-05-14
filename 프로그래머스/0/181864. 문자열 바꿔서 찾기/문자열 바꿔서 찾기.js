function solution(myString, pat) {
    myString = myString.replaceAll("A", "c")
    myString = myString.replaceAll("B", "A")
    myString = myString.replaceAll("c", "B")
    return +myString.includes(pat);
}