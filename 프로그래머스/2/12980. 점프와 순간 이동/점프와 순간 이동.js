function solution(n)
{
    var ans = 0;

    while(n != 0) {
        if(n % 2) {
            n--;
            ans++;
        }
        n /= 2;
    }

    return ans;
}