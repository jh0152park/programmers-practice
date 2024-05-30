function solution(bandage, health, attacks) {
    let delta_attack_time = [];
    const recovery = {
        "time": bandage[0],
        "hp": bandage[1],
        "extra": bandage[2],
        "max": health,
    };
    
 
    for(let i = 1; i < attacks.length; i++) {
        delta_attack_time.push(attacks[i][0] - attacks[i - 1][0]);
    }
    
    for(let i = 0; i < delta_attack_time.length; i++) {
        health -= attacks[i][1];
        if(health <= 0) {
            return -1;
        }
        
        if(delta_attack_time[i] - 1 >= recovery["time"]) {
            health += recovery["time"] * recovery["hp"];
            health += recovery["extra"];
                        
            let extra_time = delta_attack_time[i] - 1 - recovery["time"];
            if(extra_time > 0) {
                health += extra_time * recovery["hp"];
                health += parseInt(extra_time / recovery["time"]) * recovery["extra"];
            }
            
        } else {
            health += (delta_attack_time[i] - 1) * recovery["hp"];
        }
        
        if(health > recovery["max"]) {
            health = recovery["max"];
        }
    }
    health -= attacks.at(-1)[1];

    return health <= 0 ? -1 : health;
}

