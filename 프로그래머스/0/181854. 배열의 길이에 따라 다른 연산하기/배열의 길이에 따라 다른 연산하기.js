function solution(arr, n) {
    var answer = [];
    
    if(arr.length % 2) { // odd
        answer = arr.map((num, index) => {
            if(!(index % 2)) {
                return num += n
            } else {
                return num
            }
        })
    } else { // even
        answer = arr.map((num, index) => {
            if(index % 2) {
                return num += n
            } else {
                return num
            }
        })
    }
    return answer;
}