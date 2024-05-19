function solution(num_list, n) {
    let t = []
    var answer = [];
    
    for(let i = 0; i < num_list.length; i++) {
        t.push(num_list[i])
        if(t.length === n) {
            answer.push(t)
            t = []
        }
    }
    
    return answer;
}