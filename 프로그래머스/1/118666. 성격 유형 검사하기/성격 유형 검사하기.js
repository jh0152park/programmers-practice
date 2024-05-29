function solution(survey, choices) {
    var answer = '';
    let type = {
        R: 0, T: 0,
        C: 0, F: 0,
        J: 0, M: 0,
        A: 0, N: 0
    }
    let score = {
        1: 3, 2: 2, 3: 1,
        5: 1, 6: 2, 7: 3
    }
    let pair = ["RT", "CF", "JM", "AN"];
    
    for(let i = 0; i < survey.length; i++) {
        if(choices[i] !== 4) {
            if(choices[i] <= 3) {
                type[survey[i][0]] += score[choices[i]];
            } else {
                type[survey[i][1]] += score[choices[i]];
            }
        }
    }
    
    for(let personality of pair) {
        if(type[personality[0]] === type[personality[1]]) {
            answer += personality[0];
        } else {
            answer += type[personality[0]] > type[personality[1]] ? personality[0] : personality[1];
        }
    }
    
    return answer;
}