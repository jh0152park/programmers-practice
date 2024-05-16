function solution(common) {
    var answer = 0;
    
    const delta1 = common[1] - common[0];
    const delta2 = common[2] - common[1];
    
    if(delta1 === delta2) {
        return common.at(-1) + delta1;
    } else {
        const time = parseInt(delta2 / delta1);
        return common.at(-1) * time;
    }
}