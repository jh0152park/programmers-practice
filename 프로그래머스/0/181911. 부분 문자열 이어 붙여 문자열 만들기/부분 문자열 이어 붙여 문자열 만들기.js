function solution(my_strings, parts) {
    
    
    return my_strings.map((str, index) => str.slice(parts[index][0], parts[index][1]+1)).join("");
}