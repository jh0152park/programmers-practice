function compute_letter(letter, index, skips, alphabet) {
    let char = "";
    let length = alphabet.length;
    let position = alphabet.indexOf(letter);
    
    for(let i = 0; i < index; i++) {
        char = alphabet[++position % length];
        if(skips.includes(char)) {
            index++;
        }
    }
    
    return char;
}


function solution(s, skip, index) {
    var answer = '';
    let alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                    "j", "k", "l", "m", "n", "o", "p", "q", "r",
                    "s", "t", "u", "v", "w", "x", "y", "z"];    
    let skip_alphabet = skip.split("");
    
    for(let letter of s) {
        answer += compute_letter(letter, index, skip_alphabet, alphabet);
    }
    
    return answer;
}