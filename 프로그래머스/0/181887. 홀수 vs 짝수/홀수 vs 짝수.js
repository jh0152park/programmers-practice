function solution(num_list) {
    let odd_sum = 0;
    let even_sum = 0;
    num_list.forEach((n, index) => index % 2 ? odd_sum += n : even_sum += n);
    return odd_sum === even_sum ? odd_sum : odd_sum > even_sum ? odd_sum : even_sum;
}