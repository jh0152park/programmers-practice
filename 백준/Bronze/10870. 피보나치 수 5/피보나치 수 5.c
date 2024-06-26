#include <stdio.h>

int fibo(int n) {
    if(n == 0) return 0;
    if(n <= 2) return 1;
    return fibo(n - 1) + fibo(n - 2);
}

int main(int argc, const char * argv[]) {
    int n;
    
    scanf("%d", &n);
    printf("%d\n", fibo(n));
    
    return 0;
}
