function solution(a, b, c, d) {
    let cube = [a,b,c,d].sort((a,b) => a-b);
    
    a = cube[0];
    b = cube[1];
    c = cube[2];
    d = cube[3];
    
    return (
        a === d ? a * 1111      :
        a === c ? (10*a+d)**2   :
        b === d ? (10*b+a)**2   :
        a === b && c === d ? (a + c) * Math.abs(a - c) :
        a === b ? c * d :
        b === c ? a * d :
        c === d ? a * b :
        a
    )
}

