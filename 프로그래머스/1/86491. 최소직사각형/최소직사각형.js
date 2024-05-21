function solution(sizes) {
    let widths = [];
    let heights = [];
    
    sizes.forEach((size) => {
        widths.push(Math.max(...size));
        heights.push(Math.min(...size));
    })
    
    return Math.max(...widths) * Math.max(...heights);
}