function solution(players, callings) {    
    let rank = {};
    
    for(let i = 0 ; i < players.length; i++) {
        rank[players[i]] = i;
    }
    
    for(let player of callings) {
        let position = rank[player];
        let overtake = players[position - 1];
        
        players[position] = players[position - 1];
        players[position - 1] = player;
        
        rank[player]--;
        rank[overtake]++;
    }
    
    return players;
}
