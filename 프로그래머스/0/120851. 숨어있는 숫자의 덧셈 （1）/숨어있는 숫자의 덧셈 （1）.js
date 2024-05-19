function solution(my_string) {
    var answer = 0;
    let numbers = [1,2,3,4,5,6,7,8,9]
    my_string.split("").forEach(c => {
        if(numbers.includes(+c))
            answer += +c
    })
    return answer;
}