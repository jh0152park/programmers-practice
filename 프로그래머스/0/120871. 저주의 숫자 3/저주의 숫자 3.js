function solution(n) {
    let count = 1;
    let convert_num = 1;
    
    while(n > count) {
        count++;
        convert_num++;
        
        while(convert_num % 3 === 0 || String(convert_num).includes('3')) {
            convert_num++;
        }
    }
    return convert_num;
}
