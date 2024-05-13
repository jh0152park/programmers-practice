function solution(str_list) {
    if(!str_list.includes("l") && !str_list.includes("r"))
        return [];
    
    const l = str_list.indexOf("l");
    const r = str_list.indexOf("r");
    let str = ""
    
    console.log(`left index is ${l}`)
    console.log(`right index is ${r}`)
    
    if(l < 0 || r < 0) {
        if(l >= 0) {
            str = str_list.slice(0, l);
        } else if(r >= 0) {
            str = str_list.slice(r+1);
        }
    } else if(l >= 0 && r >= 0) {
        if(l < r) {
            str = str_list.slice(0, l);
        } else {
            str = str_list.slice(r+1);
        }
    }
    
    return str
}

// ["u", "r", "d"] ["d"] / 
// ["u", "l", "d"] ["u"] / 
// ["u", "d"] [] 테스트 케이스 추가해보세요