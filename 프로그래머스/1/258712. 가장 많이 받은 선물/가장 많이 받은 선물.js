function solution(friends, gifts) {
    var answer = 0;
    let history = {};
    let gift_ratio = {};
    
    for(let friend of friends) {
        history[friend] = {
            "send": {
                "count": 0,
            },
            "receive": {
                "count": 0,
            },
            "connection": []
        };
        gift_ratio[friend] = 0;
    }
    
    for(let gift of gifts) {
        let sender = gift.split(" ")[0];
        let receiver = gift.split(" ")[1];
        
        if(!(!!history[sender]["send"][receiver])) {
            history[sender]["send"][receiver] = 0;
        }
        if(!(!!history[receiver]["receive"][sender])) {
            history[receiver]["receive"][sender] = 0;
        }
        

        history[sender]["send"]["count"]++;
        history[sender]["send"][receiver]++;
        
        history[receiver]["receive"]["count"]++;
        history[receiver]["receive"][sender]++;
        
        history[sender]["connection"].push(receiver);
        history[receiver]["connection"].push(sender);
    }
    
    
    for(let friend of friends) {
        gift_ratio[friend] = history[friend]["send"]["count"] - history[friend]["receive"]["count"];
        history[friend]["connection"] = Array.from(new Set(history[friend]["connection"]));
    }
    
    // console.log(history);
    
    for(let friend of friends) {
        let gift = 0;
        
        for(let key of Object.keys(history[friend]["send"])) {
            if(key === "count") continue;
            
            if(history[friend]["send"][key] > history[friend]["receive"][key]) {
                gift++;
            } else if(history[friend]["send"][key] > 0 && !(!!history[friend]["receive"][key])) {
                gift++;
            } else if(history[friend]["send"][key] === history[friend]["receive"][key]) {
                if(gift_ratio[friend] > gift_ratio[key]) {
                    gift++;
                }
            }
        }
        
        let no_connection = friends.filter((f) => ![...history[friend]["connection"], friend].includes(f));
        for(let f of no_connection) {
            if(gift_ratio[friend] > gift_ratio[f]) {
                gift++;
            }
        }
        
        // console.log(friend, gift);
        if(gift > answer) {
            answer = gift;
        }
    }
    
    return answer;
}