function solution(my_string) {
    let sum = 0;
    let mode = true;
    
    my_string.split(" ").forEach(c => {
        if(c === "+" || c === "-") {
            if(c === "+")   mode = true;
            else            mode = false;
        } else {
             if(mode)   sum += +c
             else       sum -= +c
        }
    })

    return sum;
}