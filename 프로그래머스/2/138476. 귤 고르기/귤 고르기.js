function solution(k, tangerine) {
    let pick = 0;
    let mandarin = new Array(Math.max(...tangerine) + 1).fill(0);
    
    for(let i = 0; i < tangerine.length; i++) {
        mandarin[tangerine[i]]++;
        if(mandarin[tangerine[i]] >= k) {
            return 1;
        }
    }
    
    mandarin.sort((a, b) => b - a);
    
    for(let i = 0; i < mandarin.length; i++) {
        pick += mandarin[i];
        if(pick >= k) {
            return i + 1;
        }
    }

}