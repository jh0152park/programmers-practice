function solution(chicken) {
    var answer = 0;
    
    let service = 0;
    let coupon = 0;
    
    while(chicken) {
        service += parseInt(chicken / 10);
        coupon += parseInt(chicken % 10);
        chicken = parseInt(chicken / 10);
    }
    
    while(coupon >= 10) {
        service += parseInt(coupon / 10);
        coupon = parseInt(coupon % 10) + parseInt(coupon / 10);
        
    }
    
    return parseInt(coupon / 10) + service;
}