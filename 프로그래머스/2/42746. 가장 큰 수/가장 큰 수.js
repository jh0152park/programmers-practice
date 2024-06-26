function solution(numbers) {
    numbers = numbers.map((number) => number + "");
    numbers.sort(function(a, b) {
        if(a.repeat(3) > b.repeat(3))   return -1;
        return 1;
    });
    

    let answer = numbers.join("");

    return answer[0] === "0" ? "0" : answer;
}