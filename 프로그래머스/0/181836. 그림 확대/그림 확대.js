function solution(picture, k) {
    var answer = [];
    
    for(let i = 0; i < picture.length; i++) {
        let str = "";
        for(let j = 0; j < picture[i].length; j++) {
            str += picture[i][j].repeat(k);
        }
        for(let j = 0; j < k; j++) {
            answer.push(str);
        }
    }
    
    return answer;
}