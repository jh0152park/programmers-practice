function operation(order) {
    switch(order) {
        case "w":
            return 1;
        case "s":
            return -1;
        case "d":
            return 10;
        case "a":
            return -10;
    }
}

function solution(n, control) {
    control.split("").forEach((o) => n += operation(o));
    return n;
}