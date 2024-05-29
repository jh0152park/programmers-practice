function solution(board, moves) {
    var answer = 0;
    let bucket = [];
    
    for(let move of moves) {
        for(let row of board) {
            if(row[move - 1] !== 0) {
                bucket.push(row[move - 1]);
                row[move - 1] = 0;
                break;
            }
        }
    }
    
    let temp = [];
    for(let doll of bucket) {
        temp.push(doll);
        
        if(temp.length < 2) {
            continue;
        }
        
        if(temp.at(-1) === temp.at(-2)) {
            answer += 2;
            temp.pop();
            temp.pop();
        }
    }
    
    return answer;
}
