function solution(citations) {
    var answer = 0;
    let thesis = citations.length;
    
    citations.sort((a, b) => a - b);
    
    for(let h = 0; h <= citations.at(-1); h++) {
        let citation = 0;
        // h번 보다 적게 인용된 것들
        for(let i = 0; i < thesis; i++) {
            if(citations[i] < h)    citation++;
            else                    break;
        }
        
        if(thesis - citation >= h && citation <= h) {
            answer = h;
        }
    }
    
    return answer;
}