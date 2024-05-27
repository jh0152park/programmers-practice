function compute_ratio(process, current_stage) {
    let clear = 0;
    
    if(!(!!process[current_stage])) {
        return 0;
    }
    
    for(let stage of Object.keys(process)) {
        if(stage >= current_stage) {
            clear += process[stage];
        }
    }
    
    return process[current_stage] / clear;
}


function solution(N, stages) {
    var answer = [];
    let process = {};
    let fail_ratio = [];
    
    for(let user of stages) {
        if(!(!!process[user])) {
            process[user] = 0;
        }
        process[user]++;
    }
    
    
    for(let stage = 1; stage <= N; stage++) {
        fail_ratio.push(compute_ratio(process, stage));
    }
    
    for(let i = 0; i < fail_ratio.length; i++) {
        let max = -1;
        let index = 0;
        
        for(let j = 0; j < fail_ratio.length; j++) {
            if(fail_ratio[j] > max) {
                index = j + 1;
                max = fail_ratio[j];
            }
        }
        
        answer.push(index);
        fail_ratio[index - 1] = -1;
    }
    
    
    return answer;
}