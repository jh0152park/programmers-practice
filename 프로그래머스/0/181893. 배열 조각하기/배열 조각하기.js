function solution(arr, query) {    
    query.forEach((q, i) => {
        if(i % 2 === 0) arr = arr.slice(0, q+1);
        else            arr = arr.slice(q);
    })
    
    return arr;
}