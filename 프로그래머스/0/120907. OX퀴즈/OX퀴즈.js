function compute(num1, num2, oper) {
    switch(oper) {
        case "-":
            return num1 - num2;
        case "+":
            return num1 + num2;
    }
}

function solution(quiz) {
    let result = []
    
    quiz.forEach(q => {
        const form = q.split(" ")
        const num1 = form[0]
        const num2 = form[2]
        const oper = form[1]
        const answer = form.at(-1)
                
        if(compute(+num1, +num2, oper) === +answer) {
            result.push("O")
            // console.log("O")
        } else {
            result.push("X")
            // console.log("X")
        }
            
    })
    
    return result;
}