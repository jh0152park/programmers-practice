function solution(keyinput, board) {
    var position = [0, 0];
    
    let max_x = (board[0] - 1) * 0.5
    let max_y = (board[1] - 1) * 0.5;
    
    for(let dir of keyinput) {
        if(dir === "left" && position[0] > -max_x) {
            position[0]--;
        } else if(dir === "right" && position[0] < max_x) {
            position[0]++;
        } else if(dir === "up" && position[1] < max_y) {
            position[1]++;
        } else if(dir === "down" && position[1] > -max_y) {
            position[1]--;
        }
    }
    
    return position;
}