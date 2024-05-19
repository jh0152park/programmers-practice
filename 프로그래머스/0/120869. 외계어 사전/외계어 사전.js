function solution(spell, dic) {
    var answer = 0;
    
    spell = spell.sort().join("")
    console.log(spell)
    
    for(let str of dic) {
        str = Array.from(new Set(str.split(""))).sort().join("")
        if(str === spell)   return 1;
    }
    
    return 2;
}