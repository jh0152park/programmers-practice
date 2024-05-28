function solution(keymap, targets) {
    var answer = [];
    let keypad = {};
    
    for(let keys of keymap) {
        let press = 0;
        for(let key of keys) {
            press++;
            if(!(!!keypad[key])) {
                keypad[key] = press;
                continue;
            }
            
            if(keypad[key] > press) {
                keypad[key] = press;
            }
        }
    }
    
    for(let target of targets) {
        let press = 0;
        for(let char of target) {
            if(!(!!keypad[char])) {
                press = -1;
                break;
            }
            press += keypad[char];
        }
        answer.push(press);
    }
    
    return answer;
}