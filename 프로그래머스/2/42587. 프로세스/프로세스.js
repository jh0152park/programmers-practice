function solution(priorities, location) {
    let task = [];
    
    for(let i = 0; i < priorities.length; i++) {
        for(let j = 0; j < priorities.length; j++) {
            if(Math.max(...priorities) === priorities[j]) {
                task.push(j);
                priorities[j] = 0;
            }
            if(task.length === priorities.length)
                break;
        }
        if(task.length === priorities.length)
                break;
    }
    
    return task.indexOf(location) + 1;
}
