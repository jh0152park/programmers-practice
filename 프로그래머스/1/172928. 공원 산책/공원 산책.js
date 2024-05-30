function is_can_move(x, y, order, map, x_length, y_length) {
    let dir = order.split(" ")[0];
    let dis = +order.split(" ")[1];
        
    if(dir === "W" && x - dis < 0)          return false;
    if(dir === "E" && x + dis >= x_length)  return false;
    if(dir === "N" && y - dis < 0)          return false;
    if(dir === "S" && y + dis >= y_length)  return false;
    
    if(dir === "E") {
        for(let i = 1; i <= dis; i++) {
            if(map[y][x + i] === "X") {
                return false;
            }
        }
        return true;
    }
    
    if(dir === "W") {
        for(let i = 1; i <= dis; i++) {
            if(map[y][x - i] === "X") {
                return false;
            }
        }
        return true;
    }
    
    if(dir === "S") {
        for(let i = 1; i <= dis; i++) {
            if(map[y + i][x] === "X") {
                return false;
            }
        }
        return true;
    }
    
    if(dir === "N") {
        for(let i = 1; i <= dis; i++) {
            if(map[y - i][x] === "X") {
                return false;
            }
        }
        return true;
    }
}


function solution(park, routes) {
    let x = -1;
    let y = -1;
    let x_length = park[0].length;
    let y_length = park.length;
    
    for(let i = 0; i < y_length; i++) {
        for(let j = 0; j < x_length; j++) {
            if(park[i][j] === "S") {
                x = j;
                y = i;
                i = y_length;
                break;
            }
        }
    }
    
    for(let route of routes) {
        if(is_can_move(x, y, route, park, x_length, y_length)) {
            let dir = route.split(" ")[0];
            let dis = +route.split(" ")[1];
            
            if(dir === "E") {
                x += dis;
            } else if(dir === "W") {
                x -= dis;
            } else if(dir === "S") {
                y += dis;
            } else {
                y -= dis;
            }
        }
    }
    
    return [y, x];
}