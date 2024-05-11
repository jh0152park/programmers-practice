function solution(my_string, queries) {
    var answer = '';
    let str = my_string.split("");
    for(let i = 0; i < queries.length; i++) {
        str = [
            ...str.slice(0, queries[i][0]),
            ...str.slice(queries[i][0], queries[i][1]+1).reverse(),
            ...str.slice(queries[i][1]+1)
        ]
    }
    
    return str.join("");
}