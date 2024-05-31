function translate(str) {
    let loop = 0;
    let zero = 0;
    let length = 0;
    
    while(str !== "1") {
        loop++;
        length = str.length;
        
        str = str.split("").filter((s) => s !== "0");
        zero += length - str.length;
        str = str.length.toString(2);
    }

    return [loop, zero];
}


function solution(s) {
    return translate(s);
}