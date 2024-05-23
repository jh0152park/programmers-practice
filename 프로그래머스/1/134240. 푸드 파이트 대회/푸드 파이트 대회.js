function solution(food) {
    let answer = "";
    let reverse = "";
    
    for(let i = 1; i < food.length; i++) {
        let kcal = food[i];
        
        if(kcal % 2) {
            kcal -= 1;
        }
        
        if(kcal > 0) {
            for(let j = 0; j < kcal / 2; j++) {
                answer += i + "";
            }
        }
    }
    
    reverse = answer.split("").reverse().join("");

    return answer + "0" + reverse;
}