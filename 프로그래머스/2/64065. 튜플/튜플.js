function solution(s) {
    var answer = [];
    let str = s.slice(2, s.length - 2);
    let elements = str.split("},{");
    let lengths = elements.map((ele) => ele.replaceAll(",", "").length).sort((a, b) => a - b);
    
    console.log(elements);
    console.log(lengths);
    
    let check = {};
    for(let length of lengths) {
        for(let element of elements) {
            let numbers = element.replaceAll(",", "");
            
            if(numbers.length === length) {
                for(let num of element.split(",")) {
                    if(!(!!check[num])) {
                        check[num] = true;
                        answer.push(+num);
                    }
                }
            }
        }
    }
    
    
    return answer;
}
