function solution(arr) {
    let pow_list = [1,2,4,8,16,32,64,128,256,512,1024,2048];
    let target_length = 0;
    
    for(len of pow_list) {
        if(len >= arr.length) {
            target_length = len;
            break;
        }
    }
    
    const initial_length = arr.length;
    for (let i = 0; i < target_length - initial_length; i++) {
        arr.push(0)
    }

    return arr;
}