function solution(arr) {
    arr.sort((a, b) => a - b);
    let max = arr.at(-1);
    
    while(true) {
        let clear = true;
        for(let num of arr) {
            if(max % num) {
                clear = false;
                break;
            }
        }
        
        if(clear) {
            return max;
        }
        
        max += arr.at(-1);
    }
}