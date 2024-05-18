function solution(score) {
    var answer = [];
    
    const averages = score.map(s => (s[0]+s[1])*0.5);
    const rank = [...averages].sort((a, b) => b - a);
    
    console.log(averages);
    console.log(rank)
    
    averages.forEach(average => answer.push(rank.indexOf(average)+1))
    
    
    return answer;
}