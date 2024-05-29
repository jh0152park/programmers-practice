function compute_to_day(date) {
    date = date.split(".");
    
    let year = +date[0] * 12 * 28;
    let month = +date[1] * 28;
    let day = +date[2] + year + month;

    return day;
}


function compute_month_to_day(month) {
    return +month * 28;
}


function solution(today, terms, privacies) {
    var answer = [];
    let expire = {};
    let day_of_today = compute_to_day(today);
    
    for(let term of terms) {
        expire[term.split(" ")[0]] = term.split(" ")[1];
    }
    
    
    
    let num = 0;
    for(let privacie of privacies) {
        num++;
        let date = privacie.split(" ")[0];
        let type = privacie.split(" ")[1];
        let criteria = compute_to_day(date);
        let extend = compute_month_to_day(expire[type]);
             
        if(criteria + extend <= day_of_today) {
            answer.push(num);
        }
        
    }
    
    return answer;
}