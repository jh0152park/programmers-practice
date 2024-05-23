function solution(wallpaper) {
    let x_pos = [];
    let y_pos = [];
    var answer = [];
    
    for(let y = 0; y < wallpaper.length; y++) {
        for(let x = 0; x < wallpaper[y].split("").length; x++) {
            if(wallpaper[y][x] === "#") {
                x_pos.push(x);
                y_pos.push(y);
            }
        }
    }
    
    x_pos = x_pos.sort((a, b) => a - b);
    y_pos = y_pos.sort((a, b) => a - b);    
    answer = [y_pos[0], x_pos[0], y_pos.at(-1) + 1, x_pos.at(-1) + 1];

    return answer;
}