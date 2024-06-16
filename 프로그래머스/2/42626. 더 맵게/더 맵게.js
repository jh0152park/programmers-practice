var index = 0;
var index2 = 0;

function min(scoville, new_scoville) {
    if((scoville[index] ?? Infinity) <= (new_scoville[index2] ?? Infinity)) {
        return scoville[index++];
    } else {
        return new_scoville[index2++];
    }
}

function get_min_scovilles(scoville, new_scoville) {
    return [min(scoville, new_scoville), min(scoville, new_scoville)];
}


function solution(scoville, K) {
    var answer = 0;
    let new_scoville = [];
    let scoville_length = scoville.length;
    
    
    scoville.sort((a, b) => a - b);
    
    if(scoville[0] >= K) {
        return 0;
    }
        
    while(1) {
        if(((scoville_length - index) + (answer - index2)) < 2) {
            break;
        }
        
        if((scoville[index] ?? Infinity) >= K && (new_scoville[index2] ?? Infinity) >= K) {
            break;
        }
        
        answer++;

        let [min, min2] = get_min_scovilles(scoville, new_scoville);
        new_scoville.push(min2 * 2 + min);
        
        // console.log(min, min2, index, index2);
        // console.log(scoville);
        // console.log(new_scoville);
        // console.log();
    }
    
    if(scoville[index] < K || new_scoville[index2] < K) {
        return -1;
    }
    
    return answer;
}

