function solution(arr) {
    const v = arr.length;
    const h = arr[0].length;
    
    console.log(v, h);
    if(v === h)
        return arr;
    
    if(v > h) {
        for(let i = 0; i < v; i++) {
            for(let j = 0; j < v-h; j++) {
                arr[i].push(0)
            }
        }
        return arr;
    } else {
        for(let i = 0; i < h-v; i++) {
            arr.push([...Array(h).fill(0)])
        }
        return arr;
    }
    
    return ""
}