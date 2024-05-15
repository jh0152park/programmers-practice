function cost(menu) {
    if(menu.includes("americano"))  return 4500;
    else if(menu.includes("latte")) return 5000;
    else                            return 4500;
}

function solution(order) {
    var answer = 0;
    order.forEach(m => answer += cost(m));
    return answer;
}