function solution(arr1, arr2) {
    let answer = [];
    
    for(let y = 0; y < arr1.length; y++) {
        let temp = [];
        for(let x = 0; x < arr2[0].length; x++) {
            let sum = 0;
            for(let k = 0; k < arr1[0].length; k++) {
                sum += arr1[y][k] * arr2[k][x];
            }
            temp.push(sum);
        }
        answer.push(temp)
    }
    
    return answer;
}