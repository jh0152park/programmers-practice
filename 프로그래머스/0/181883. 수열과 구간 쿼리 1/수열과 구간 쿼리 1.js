function solution(arr, queries) {
    for(let i = 0; i < queries.length; i++) {
        for(let j = queries[i][0]; j <= queries[i][1]; j++) {
            arr[j]++;
        }
    }
    return arr;
}


// 입력값 〉 [1, 2, 3, 4, 5], [[2, 4]]
// 기댓값 〉 [1, 2, 4, 5, 6]