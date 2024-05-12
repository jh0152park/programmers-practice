function solution(s){
    let p = 0;
    let y = 0;
    
    for(let char of s.split("")) {
        if(char === "p" || char === "P") p++;
        if(char === "y" || char === "Y") y++;
    }
    return p === y;
}