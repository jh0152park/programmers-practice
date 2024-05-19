function solution(my_string) {
    let answer = []
    const numbers = [0,1,2,3,4,5,6,7,8,9]
    
    my_string.split("").forEach(s => {
        if(numbers.includes(+s))
            answer.push(+s)
    })
    
    return answer.sort((a,b) => a-b)
}