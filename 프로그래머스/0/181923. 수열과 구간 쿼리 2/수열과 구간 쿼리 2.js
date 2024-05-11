function solution(arr, queries) {
    var answer = [];
    
    for(let i = 0; i < queries.length; i++) {
        const temp = [];
        for(let j = queries[i][0]; j <= queries[i][1]; j++) {
            if(arr[j] > queries[i][2])
                temp.push(arr[j]);
        }
        
        temp.sort((a,b) => a-b);
        if(temp.length) {
            answer.push(temp[0])
        } else {
            answer.push(-1)
        }
    }
    
    return answer;
}