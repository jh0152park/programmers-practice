function solution(sides) {
    var answer = 0;
    
    sides = sides.sort((a, b) => a - b);
    const max1 = sides[1] - ((sides[1] + 1) - sides[0]) + 1;
    const max2 = (sides[0] + sides[1]) - 1 - sides[1];
    return max1 + max2;
}