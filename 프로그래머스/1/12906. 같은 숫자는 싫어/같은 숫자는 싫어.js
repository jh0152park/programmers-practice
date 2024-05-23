function solution(arr)
{
    let prev = -1;
    const stack = [];
    
    for(let num of arr) {
        if(num !== prev) {
            stack.push(num)
        }
        prev = num;
    }
    
    return stack;
}