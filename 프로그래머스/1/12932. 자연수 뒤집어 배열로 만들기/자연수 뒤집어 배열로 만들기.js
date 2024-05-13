function solution(n) {
    var answer = [];
    let n_arr = String(n).split("");
    
    for(let i = n_arr.length - 1; i >= 0; i--) {
        answer.push(+n_arr[i]);
    }
    
    return answer;
}