function solution(n, m, section) {
    let fill = 0;
    let wall = new Array(n + 1).fill(true);
    
    for(let i = 0; i < section.length; i++) {
        wall[section[i]] = false;
    }
    

    for(let i = 1; i < wall.length; i++) {
        if(!wall[i]) {
            fill++;
            for(let j = 0; j < m; j++) {
                wall[i + j] = true;
            }
            i += m - 1
        }
    }
    
    return fill;
}