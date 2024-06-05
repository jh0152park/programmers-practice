function solution(people, limit) {
    var answer = 0;
    let lightest = 0;
    let heavyest = people.length - 1;
    
    
    people.sort((a, b) => a - b);
    while(lightest <= heavyest) {
        if(people[lightest] + people[heavyest] <= limit) {
            lightest++;
            heavyest--;
        } else {
            heavyest--;
        }
        answer++;
    }
    
    return answer;
}