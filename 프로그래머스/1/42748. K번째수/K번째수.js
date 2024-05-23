function solution(array, commands) {
    var answer = [];
    
    for(let command of commands) {
        let from = command[0];
        let to = command[1];
        let target = command[2] - 1;
        let slice = array.slice(from - 1, to);
        
        slice = slice.sort((a, b) => a - b);
        answer.push(slice[target]);
    }
    
    return answer;
}