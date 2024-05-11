function solution(num_list) {
    let odd = []
    let even = []
    
    num_list.forEach((n) => {
        n % 2 === 0 ? even.push(n+"") : odd.push(n+"")
    })
    
    odd = +(odd.join(""))
    even = +(even.join(""))
    
    return odd + even;
}