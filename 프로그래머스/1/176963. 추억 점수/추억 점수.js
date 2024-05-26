function solution(name, yearning, photo) {
    var answer = [];
    let score = {};
    
    for(let i = 0; i < name.length; i++) {
        score[name[i]] = yearning[i];
    }
    
    photo.forEach((peoples) => {
        let sum = 0;
        peoples.forEach((people) => sum += score[people] ?? 0);
        answer.push(sum);
    })
    
    return answer;
}