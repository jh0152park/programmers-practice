function solution(s) {
    let english = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
    ]
    
    let number = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    
    for(let eng of english) {
        s = s.replaceAll(eng, number[eng]);
    }
    
    return +s;
}