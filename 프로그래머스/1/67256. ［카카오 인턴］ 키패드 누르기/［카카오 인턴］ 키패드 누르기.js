function compute_distance(from, to, keymap) {
    let x_delta = Math.abs( keymap[from]["x"] - keymap[to]["x"] );
    let y_delta = Math.abs( keymap[from]["y"] - keymap[to]["y"] );
    return x_delta + y_delta;
}


function solution(numbers, hand) {
    let left = "*";
    let right = "#";
    let press = "";
    
    const left_side = {1: true, 4: true, 7: true};
    const right_side = {3: true, 6: true, 9: true};
    const key_position = {
        1: {x: 1, y: 1}, 2: {x: 2, y: 1}, 3: {x: 3, y: 1},
        4: {x: 1, y: 2}, 5: {x: 2, y: 2}, 6: {x: 3, y: 2},
        7: {x: 1, y: 3}, 8: {x: 2, y: 3}, 9: {x: 3, y: 3},
        "*": {x: 1, y: 4}, 0: {x: 2, y: 4}, "#": {x: 3, y: 4},
    };
    

    for(let number of numbers) {
        if(!!left_side[number]) {
            left = number;
            press += "L";
        } else if(!!right_side[number]) {
            right = number;
            press += "R";
        } else {
            let l_move = compute_distance(left, number, key_position);
            let r_move = compute_distance(right, number, key_position);
            
            if(l_move === r_move) {
                press += hand[0].toUpperCase();
                if(hand[0] === "r") {
                    right = number;
                } else {
                    left = number;
                }
            } else {
                if(l_move > r_move) {
                    press += "R";
                    right = number;
                } else {
                    press += "L";
                    left = number;
                }
            }
        }
    }
    
    
    return press;
}