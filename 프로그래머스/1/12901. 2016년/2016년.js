function solution(a, b) {
    const days = {
        0: "SUN",
        1: "MON",
        2: "TUE",
        3: "WED",
        4: "THU",
        5: "FRI",
        6: "SAT"
    }
    
    const day = new Date("2016-" + String(a).padStart(2, "0") + "-" + String(b).padStart(2, "0")).getDay();
    

    return days[day];
}