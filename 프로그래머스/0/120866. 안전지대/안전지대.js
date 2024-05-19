function solution(board) {
    var answer = 0;
    let n = board.length;
    
    for(let i = 0; i < n; i++) {
        console.log(board[i])
    }
    
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
            if(board[i][j] === 1) {
                if(i - 1 >= 0 && j - 1 >= 0) // top left
                {
                    if(board[i-1][j-1] !== 1)
                        board[i-1][j-1] = 2;
                }
                if(i - 1 >= 0) // top
                {
                    if(board[i-1][j] !== 1)
                        board[i-1][j] = 2;
                }
                if(i - 1 >= 0 && j + 1 < n) // top right
                {
                    if(board[i-1][j+1] !== 1)
                        board[i-1][j+1] = 2;
                }
                if(j - 1 >= 0) // left
                {
                    if(board[i][j-1] !== 1)
                        board[i][j-1] = 2;
                }
                if(j + 1 < n) // right
                {
                    if(board[i][j+1] !== 1)
                        board[i][j+1] = 2;
                }
                if(i + 1 < n && j - 1 >= 0) // bottom left
                {
                    if(board[i+1][j-1] !== 1)
                        board[i+1][j-1] = 2;
                }
                if(i + 1 < n) // bottom
                {
                    if(board[i+1][j] !== 1)
                        board[i+1][j] = 2;
                }
                if(i + 1 < n && j + 1 < n) // bottom right
                {
                    if(board[i+1][j+1] !== 1)
                        board[i+1][j+1] = 2;
                }
            }
        }
    }
    
    console.log("//////")
    for(let i = 0; i < n; i++) {
        console.log(board[i])
    }
    
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
            if(board[i][j] === 0) answer++;
        }
    }
    
    
    return answer;
}