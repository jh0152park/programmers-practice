function solution(s){
    const stack = [];

    for(let bracket of s.split("")) {
        if(bracket === "(") stack.push(bracket);
        else {
            if(stack.length === 0) {
                return false;
            } else {
                stack.pop();
            }
        }
    }
    
    return !Boolean(stack.length);
}