function solution(strArr) {
    const lengths = [...Array(31).fill(0)];
    strArr.forEach(str => lengths[str.length]++)
    lengths.sort((a,b) => a-b)
    return lengths.at(-1);
}