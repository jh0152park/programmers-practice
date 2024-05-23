function compute(answers, player) {
    let hit = 0;
    for(let i = 0; i < answers.length; i++) {
        if(answers[i] === player[i % player.length]) {
            hit++;
        }
    }
    return hit;
}


function solution(answers) {
    let max = 0;
    let answer = [];
    const hits = [];
    const player1 = [1, 2, 3, 4, 5];
    const player2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const player3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    hits.push(compute(answers, player1));
    hits.push(compute(answers, player2));
    hits.push(compute(answers, player3));
    
    max = Math.max(...hits)
    for(let i = 0; i < 3; i++) {
        if(hits[i] === max) {
            answer.push(i + 1)
        }
    }
    
    return answer;
}