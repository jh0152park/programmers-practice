function solution(rank, attendance) {
    let sort_rank = []
    let ranking = {};
    
    rank.forEach((rank, index) => {
        if(attendance[index]) {
            ranking[rank] = index;
            sort_rank.push(rank);
        }
    })
    
    sort_rank.sort((a,b) => a-b);
    console.log(sort_rank);
    console.log(ranking);
    
    return (ranking[sort_rank[0]] * 10000) + (ranking[sort_rank[1]] * 100) + ranking[sort_rank[2]];
}

