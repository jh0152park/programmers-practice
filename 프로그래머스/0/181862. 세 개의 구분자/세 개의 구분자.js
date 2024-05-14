function solution(myStr) {
    let str = myStr.replaceAll("a", "_").replaceAll("b", "_").replaceAll("c", "_")
    
    str = str.split("_").filter(c => c !== "")
    
    return str.length ? str : ["EMPTY"];
    
}