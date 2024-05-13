function solution(t, p) {
    let answer = 0;
    let compare_numbers = [];
    
    const length = p.length;
    const numbers = t.split("");

    for(let i = 0; i <= numbers.length - length; i++) {
        let str = "";
        for(let j = i; j < i + length; j++) {
            str += numbers[j];
        }
        compare_numbers.push(+str);
    }
    
    for(let num of compare_numbers) {
        if(num <= +p) {
            answer++;
        }
    }

    return answer;
}