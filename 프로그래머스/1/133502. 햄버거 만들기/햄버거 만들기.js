function is_it_hamburger(hamburger) {
    if(hamburger.at(-4) === 1 &&
       hamburger.at(-3) === 2 &&
       hamburger.at(-2) === 3 &&
       hamburger.at(-1) === 1) {
        return true;
    }
    return false;
}


function solution(ingredient) {
    let answer = 0;
    let hamburger = [];
    
    for(let food of ingredient) {
        hamburger.push(food);
        
        if(hamburger.length < 4) {
            continue;
        }
        
        if(is_it_hamburger(hamburger)) {
            answer++;
            hamburger.pop();
            hamburger.pop();
            hamburger.pop();
            hamburger.pop();
        }
    }
    
    return answer;
}

