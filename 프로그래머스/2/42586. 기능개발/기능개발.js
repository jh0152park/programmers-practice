function solution(progresses, speeds) {
    let release = [];
    let left_day = [];
    
    for(let i = 0; i < progresses.length; i++) {
        left_day.push(Math.ceil((100 - progresses[i]) / speeds[i]));
    }
    
    
    let day = 1;
    let left = left_day.shift();
    while(left_day.length !== 0) {
        if(left >= left_day[0]) {
            day++;
            left_day.shift();
        } else {
            release.push(day);
            left = left_day.shift();
            day = 1;
        }
    }
    release.push(day);

    return release;
}
