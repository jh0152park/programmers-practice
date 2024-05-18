function solution(sides) {
    sides.sort((a, b) => a - b);
    if(sides[2] < sides[0] + sides[1])
        return 1;
    return 2;
}