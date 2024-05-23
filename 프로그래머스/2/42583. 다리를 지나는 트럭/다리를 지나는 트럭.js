function solution(bridge_length, weight, truck_weights) {
    let second = 0;
    let next_truct = 0;
    let current_weight = 0;
    let bridge = new Array(bridge_length).fill(0);
    
    while(truck_weights.length !== 0) {
        second++;
        
        // truct escape bridge
        if(bridge[0] != 0) {
            current_weight -= bridge[0];
        }
        
        // truck move forward
        bridge.shift();
        bridge.push(0);
        
        next_truct = truck_weights[0];
        // next truck on bridge
        if(next_truct + current_weight <= weight) {
            bridge[bridge.length - 1] = truck_weights.shift();
            current_weight += next_truct;
        }
    }
    return second + bridge_length;
}