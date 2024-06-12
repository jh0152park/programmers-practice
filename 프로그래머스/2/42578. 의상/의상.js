function solution(clothes) {
    var answer = 1;
    let style = {};
    
    for(let clothe of clothes) {
        if(!(!!style[clothe[1]])) {
            style[clothe[1]] = 0;
        }
        style[clothe[1]]++;
    }
    
    for(let item of Object.keys(style)) {
        answer *= ++style[item];
    }
    
    return --answer;
}

/*
a b c
1 2
=> a1 a2 b1 b2 c1 c2
=> 3 * 2

안입는 경우도 있음

*/