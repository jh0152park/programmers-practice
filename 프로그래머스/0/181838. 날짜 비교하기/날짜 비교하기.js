function solution(date1, date2) {
    // 1999년 12월 31일 과 2000년 1월 1일을 비교한다면 어떨까요? : )
    
    let sum1 = 0;
    let sum2 = 0;
    sum1 += date1[0] * 365;
    sum2 += date2[0] * 365;
    sum1 += date1[1] * 30;
    sum2 += date2[1] * 30;
    sum1 += date1[2];
    sum2 += date2[2];
    
    return sum1 < sum2 ? 1 : 0;
}