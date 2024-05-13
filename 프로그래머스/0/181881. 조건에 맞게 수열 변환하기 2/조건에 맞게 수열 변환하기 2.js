function isSame(arr, arr2) {
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] !== arr2[i])  return false;
    }
    return true;
}

function solution(arr) {
    var answer = 0;
    
    while(true) {
        let before = [...arr];
        for(let i = 0; i < arr.length; i++) {
            if(arr[i] >= 50 && arr[i] % 2 === 0) {
                arr[i] /= 2;
            }
            else if(arr[i] < 50 && arr[i] % 2) {
                arr[i] *= 2;
                arr[i] += 1;
            }
        }
        
        if(isSame(arr, before)) break;
        answer++;
    }
    
    return answer;
}