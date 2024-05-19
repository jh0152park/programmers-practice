function get_inclination(pos1, pos2) {
    let x1 = pos1[0];
    let y1 = pos1[1];
    let x2 = pos2[0];
    let y2 = pos2[1];
    return (Math.abs(y2-y1) / Math.abs(x2-x1))
}


function solution(dots) {
    if(get_inclination(dots[0], dots[1]) === get_inclination(dots[2], dots[3]))
        return 1;
    if(get_inclination(dots[0], dots[2]) === get_inclination(dots[1], dots[3]))
        return 1;
    if(get_inclination(dots[0], dots[3]) === get_inclination(dots[1], dots[2]))
        return 1;
    return 0;

}