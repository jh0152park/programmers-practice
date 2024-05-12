function solution(my_string, s, e) {
    const reverse_str = my_string.slice(s,e+1).split("").reverse();
    
    // console.log(my_string.slice(0,s));
    // console.log(reverse_str.join(""));
    // console.log(my_string.slice(e+1));
    
    return my_string.slice(0,s)+reverse_str.join("")+my_string.slice(e+1)
}