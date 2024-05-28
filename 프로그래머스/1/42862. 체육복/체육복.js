function solution(n, lost, reserve) {
    lost = lost.sort((a, b) => a - b);
    reserve = reserve.sort((a, b) => a - b);
    let students = new Array(n + 2).fill(0);
    
    for(let student of lost) {
        students[student]--;
    }
    
    for(let student of reserve) {
        students[student]++;
    }
        
    for(let i of lost) {        
        if(students[i] === -1) {
            if(students[i - 1] > 0) {
                students[i]++;
                students[i - 1]--;
            } else if(students[i + 1] > 0) {
                students[i]++;
                students[i + 1]--;
            } else {
                n--;
            }
        }
    }
    
    return n;
}

