function solution(s)
{
    let str = [];
    
    for(let char of s) {
        if(str.length > 0 && str.at(-1) === char) {
            str.pop();
        } else {
            str.push(char);
        }
    }
    
    return str.length > 0 ? 0 : 1;
}