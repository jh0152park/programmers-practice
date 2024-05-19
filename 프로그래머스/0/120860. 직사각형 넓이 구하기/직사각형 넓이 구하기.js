function solution(dots) {
    let x = []
    let y = []
    
    dots.forEach(p => {
        x.push(p[0])
        y.push(p[1])
    })
    
    x = x.sort((a, b) => a - b)
    y = y.sort((a, b) => a - b)
    
    let dx = x[3] - x[0]
    let dy = y[3] - y[0]
    
    
    return dx * dy;
}