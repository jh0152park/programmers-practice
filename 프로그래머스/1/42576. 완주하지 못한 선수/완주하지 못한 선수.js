function solution(participant, completion) {
    let completed_runner = {};
    
    for(let runner of completion) {
        if(!(!!completed_runner[runner])) {
            completed_runner[runner] = 0;
        }
        completed_runner[runner]++;
    }
    
    for(let runner of participant) {
        if(!(!!completed_runner[runner])) {
            return runner;
        }
        if(completed_runner[runner] <= 0) {
            return runner;
        }
        completed_runner[runner]--;
    }
}