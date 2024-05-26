function combinations(items, set) {
    if(set === 1) {
        return items.map((item) => [item]);
    }
    
    let results = [];
    items.forEach((item, index) => {
        let left = items.slice(index + 1);
        let combination = combinations(left, set - 1);
        combination.forEach((combi) => results.push([item, ...combi]));
    })
    
    return results;
}


function solution(nums) {
    let remove_overlap = Array.from(new Set(nums));
    
    if(remove_overlap.length <= nums.length / 2) {
        return remove_overlap.length;
    }
    return nums.length / 2;
    
//     let max = 0;
//     let poketmons = combinations(nums, nums.length / 2);
    
//     poketmons.forEach((poketmon) => {
//         let remove_overlap = Array.from(new Set(poketmon))
//         if(remove_overlap.length > max) {
//             max = remove_overlap.length;
//         }
//     })
    
//     return max;
}