function solution(s) {    
    let chars = {};
    let str = []
    
    s.split("").forEach(c => {
        if(chars[c]) {
            chars[c]++;
        } else {
            chars[c] = 1;
        }
    })
    
    for(const [key, value] of Object.entries(chars)) {
        if(value === 1)
            str.push(key)
    }
    
    return str.sort().join("")
}