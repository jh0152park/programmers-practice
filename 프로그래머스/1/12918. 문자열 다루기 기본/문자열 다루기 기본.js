function solution(s) {
    if(s.length === 4 || s.length === 6) {
        const str = s.split("");
    const numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
        
    for(let i = 0; i < str.length; i++) {
        if(!numbers.includes(str[i])) {
            return false;
        }
    }
    
    return true;
    } else {
        return false;
    }
    
    
}