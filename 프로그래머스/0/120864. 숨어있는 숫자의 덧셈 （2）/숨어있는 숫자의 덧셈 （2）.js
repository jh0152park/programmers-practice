function solution(my_string) {
    let sum = 0;
    const nums = "0123456789".split("")
    
    let new_string = my_string.split("").map(s => {
        if(nums.includes(s)) {
            return s;
        }
        return "*"
    })
    
    new_string.join("").split("*").forEach(n => {
        if(n !== "") sum += +n;
    })
    
    return sum;
}