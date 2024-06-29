function solution(n, words) {
    let said = {};
    let player = 1;
    let player_turn = {};
    let previous = words.shift();
    
    said[previous] = true;
    player_turn[player] = 1;
    for(let word of words) {
        player = (++player % n) || n;
        player_turn[player] = (player_turn[player] || 0) + 1;
        
        if((previous.at(-1) !== word[0]) || (said[word])) {
            return [player, player_turn[player]];
        }
        
        previous = word;
        said[word] = true;
    }
    

    return [0, 0];
}