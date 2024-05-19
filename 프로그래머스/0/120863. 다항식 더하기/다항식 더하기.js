function solution(polynomial) {
    var answer = '';
    let x = 0;
    let num = 0;
    
    polynomial = polynomial.replaceAll(" ", "").split("+")
    console.log(polynomial)
    
    polynomial.forEach(c => {
        if(c.includes("x")) {
            if(c === "x") {
                x += 1
            } else {
                x += +c.split("x")[0]
            }
        } else {
            num += +c
        }
    })
    
    if(x > 0 && num > 0) {
        if(x === 1)
            return `x + ${num}`
        else
            return `${x}x + ${num}`
    } else if(x > 0 && num === 0) {
        if(x === 1)
            return `x`
        else
            return `${x}x`
    } else {
        return `${num}`
    }
    
}