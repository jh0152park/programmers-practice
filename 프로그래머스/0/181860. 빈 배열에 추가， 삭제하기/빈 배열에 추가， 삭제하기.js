function solution(arr, flag) {
    var answer = [];
    
    for(let f in flag) {
        if(flag[f]) {
            for(let i = 0; i < arr[f]; i++) {
                answer.push(arr[f]);
                answer.push(arr[f]);
            }
        } else {
            for(let i = 0; i < arr[f]; i++) {
                answer.pop();
            }
        }
    }
    
    return answer;
}