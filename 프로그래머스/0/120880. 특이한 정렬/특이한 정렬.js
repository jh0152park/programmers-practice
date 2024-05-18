function solution(numlist, n) {
    var answer = [];
    
    let delta = [];
    let delta_group = {};
    let sort_list = numlist.sort((a, b) => b - a);

    sort_list.forEach(num => delta.push(Math.abs(num-n)));
    
    console.log(sort_list);
    console.log(delta);
    
    for(let i = 0; i < delta.length; i++) {
        if(!(!!delta_group[delta[i]])) {
            delta_group[delta[i]] = [];
        }
        delta_group[delta[i]].push(sort_list[i]);
    }
    
    console.log(delta_group)
    
    delta = Object.keys(delta_group).sort((a, b) => a - b);
    
    for(let d of delta) {
        delta_group[d].forEach(n => answer.push(n))
    }
    
    
    return answer;
}