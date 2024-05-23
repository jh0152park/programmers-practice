function add_zero(bin, gap) {
    for(let i = 0; i < gap; i++) {
        bin = "0" + bin;
    }
    return bin;
}


function solution(n, arr1, arr2) {
    var answer = [];
    
    for(let i = 0; i < n; i++) {
        let bin1 = arr1[i].toString(2) + "";
        let bin2 = arr2[i].toString(2) + "";
        
        bin1 = add_zero(bin1, n - bin1.length);
        bin2 = add_zero(bin2, n - bin2.length);
        
        let map = "";
        for(let j = 0; j < n; j++) {
            map += +bin1[j] + +bin2[j] === 0 ? " " : "#";
        }
        answer.push(map);
    }
    
    return answer;
}