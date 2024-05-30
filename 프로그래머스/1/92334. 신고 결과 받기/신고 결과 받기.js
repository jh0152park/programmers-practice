function is_deteced(people, th, report_count) {
    return report_count[people] >= th ? true : false;
}


function solution(id_list, report, k) {
    var answer = [];
    let history = {};
    let report_count = {};
    
    report = Array.from(new Set(report));
    for(let report_ of report) {
        let id = report_.split(" ")[0];
        let target = report_.split(" ")[1];
        
        if(!(!!history[id])) {
            history[id] = [];
        }
    
        if(!(!!report_count[target])) {
            report_count[target] = 0;
        }
        
        history[id].push(target);
        report_count[target]++;
    }
     
    for(let id of id_list) {
        let detected = 0;
        if(!!history[id]) {
            let my_report_list = history[id];
            // my_report_list = Array.from(new Set(my_report_list));

            for(let reported_id of my_report_list) {
                if(is_deteced(reported_id, k, report_count)) {
                    detected++;
                }
            }
        }
        answer.push(detected);
    }
    
    return answer;
}